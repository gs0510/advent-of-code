def run():
    data = open('input.txt').readlines()
    rules = {}
    for d in data:
        bag, hold = d.replace('bags', 'bag').strip('.\n').split(' contain ')
        rules[bag] = {}
        if hold != 'no other bag':
            for h in hold.split(', '):
                num, color = h.split(' ', 1)
                rules[bag][color] = int(num)

    def can_contain(color, bag):
        if not rules[bag]:
            return False
        elif color in rules[bag]:
            return True
        else:
            return True in [can_contain(color, next) for next in rules[bag]]

    def contains(color):
        if not rules[color]:
            return 0
        res = 0
        for bag in rules[color]:
            res = res + rules[color][bag] * (contains(bag) + 1)
        return res

    print([can_contain('shiny gold bag', bag) for bag in rules].count(True))
    print(contains('shiny gold bag'))


if __name__ == "__main__":
    run()
