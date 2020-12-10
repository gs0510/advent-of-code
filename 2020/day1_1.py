
def run():
    data = sorted(map(int, open('input.txt', 'r').read().split('\n')))
    one = 0
    two = len(data) - 1
    while one <= two:
        if data[one] + data[two] == 2020:
            return data[one] * data[two]
        elif data[one] + data[two] > 2020:
            two = two - 1
        else:
            one = one + 1


if __name__ == "__main__":
    print(run())
