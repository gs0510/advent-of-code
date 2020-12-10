import re


def check_if_terminates(data):
    index = 0
    acc = 0
    seen = set()
    while index < len(data) and index not in seen:
        seen.add(index)
        num = int(re.findall(r'\d+', data[index])[0])
        if 'nop' in data[index]:
            index = index + 1
        elif 'acc' in data[index]:
            if '+' in data[index]:
                acc = acc + num
            else:
                acc = acc - num
            index = index + 1
        elif 'jmp' in data[index]:
            if '+' in data[index]:
                index = index + num
            else:
                index = index - num

    return acc, index >= len(data)


def replace_ins(data):
    deep_copy = list()
    for d in data:
        deep_copy.append(d)

    for index in range(len(deep_copy)):
        if 'nop' or 'jmp' in deep_copy[index]:
            if 'nop' in deep_copy[index]:
                deep_copy[index] = deep_copy[index].replace('nop', 'jmp')
            else:
                deep_copy[index] = deep_copy[index].replace('jmp', 'nop')
            acc, terminates = check_if_terminates(deep_copy)

            if terminates:
                return acc
            else:
                if 'nop' in deep_copy[index]:
                    deep_copy[index] = deep_copy[index].replace('nop', 'jmp')
                else:
                    deep_copy[index] = deep_copy[index].replace('jmp', 'nop')


if __name__ == "__main__":
    data = open('input.txt').readlines()
    print(replace_ins(data))
