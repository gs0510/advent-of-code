from collections import Counter


def read_and_parse_input():
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
    return number_list, char_list, string_list


def run():
    number_list, char_list, string_list = read_and_parse_input()
    valid = 0
    for i, string in enumerate(string_list):
        count_dict = Counter(string)
        if number_list[i][0] <= count_dict[char_list[i]] <= number_list[i][1]:
            valid = valid + 1
    return valid


if __name__ == "__main__":
    print(run())
