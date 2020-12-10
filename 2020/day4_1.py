def run():
    data = open('input.txt', 'r').read().split('\n\n')
    fields = ['ecl', 'pid', 'eyr', 'byr', 'iyr', 'hcl', 'hgt']

    valid = 0
    for string in data:
        is_valid = True
        for field in fields:
            if field not in string:
                is_valid = False
                break

        if is_valid:
            valid = valid + 1
    return valid


if __name__ == "__main__":
    print(run())
