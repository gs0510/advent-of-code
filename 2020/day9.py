

def part1(data, preamble_size):
    curr = 0
    for index in range(preamble_size, len(data)):
        curr = data[index]
        exists = False
        for i in range(index - preamble_size, index - 1):
            for j in range(i + 1, index):
                if data[i] + data[j] == curr:
                    exists = True
                    break
        if not exists:
            return index, curr


def part2(data, invalid_num, invalid_index):
    sums = [data[0]]
    for index in range(1, len(data)):
        sums = sums + [sums[index - 1] + data[index]]

    for i in range(invalid_index - 1):
        for j in range(i + 1, invalid_index):
            if sums[j] - sums[i] == invalid_num:
                return max(data[i + 1:j + 1]) + min(data[i + 1:j + 1])

    return 0


if __name__ == "__main__":
    data = list(map(int, open('input.txt', 'r').read().split()))
    print(part1(data, 25))
    print(part2(data, 57195069, 548))
