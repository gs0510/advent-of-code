def part1(data):
    data = [0] + data + [max(data) + 3]
    diff = [data[i] - data[i - 1] for i in range(1, len(data))]
    return diff.count(1) * diff.count(3)


def part2(data):
    def rec(val, d, res):
        combinations = 0
        if val == d[-1]:
            return 1
        for i in range(1, 4):
            if val + i in d:
                if val + i not in res:
                    res[val + i] = rec(val + i, d, res)
                combinations += res[val + i]
        return combinations
    return rec(0, data, {})


data = sorted(list(map(int, open('input.txt', 'r').read().split())))
print(part1(data))
print(part2(data))
