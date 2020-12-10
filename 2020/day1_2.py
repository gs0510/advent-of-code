def run():
    data = sorted(map(int, open('input.txt', 'r').read().split('\n')))
    for curr in range(0, len(data) - 1):
        one = curr + 1
        two = len(data) - 1
        while one <= two:
            if data[curr] + data[one] + data[two] == 2020:
                return data[curr] * data[one] * data[two]
            elif data[curr] + data[one] + data[two] > 2020:
                two = two - 1
            else:
                one = one + 1


if __name__ == "__main__":
    print(run())
