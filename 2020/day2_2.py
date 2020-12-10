from collections import Counter


def run():
    data = open('input.txt', 'r').read().split('\n')
    number_list = []
    char_list = []
    string_list = []
    for inp in data:
        strings = inp.split(' ')
        numbers_split = strings[0].split('-')
        number_list = number_list + \
            [(int(numbers_split[0]), int(numbers_split[1]))]
        char_list = char_list + [strings[1][0]]
        string_list = string_list + [strings[2]]

    valid = 0
    for i, string in enumerate(string_list):
        index1 = number_list[i][0] - 1
        index2 = number_list[i][1] - 1
        curr_char = char_list[i]
        if not (string[index1] == curr_char and string[index2] == curr_char) and (
                string[index1] == curr_char or string[index2] == curr_char):
            valid = valid + 1

    return valid


if __name__ == "__main__":
    print(run())
