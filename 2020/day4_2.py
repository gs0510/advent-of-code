import re


def run():
    passports = [
        p.replace(
            ' ',
            '\n') for p in open(
            'input.txt',
            'r').read().split('\n\n')]
    passports = [dict(f.split(':') for f in p.split('\n')) for p in passports]

    constraints = {
        'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
        'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
        'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
        'hgt': lambda x: (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76) or (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193),
        'hcl': lambda x: re.match(r'#[a-f0-9]{6}', x),
        'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda x: len(x) == 9 and x.isdigit()
    }

    def is_valid(p):
        return all(f in p for f in constraints.keys()) and all(
            constraints[f](p[f]) for f in constraints.keys())

    valid = sum(is_valid(p) for p in passports)

    return valid


if __name__ == "__main__":
    print(run())
