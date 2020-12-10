def run():
    data = open('input.txt', 'r').read().split('\n')
    b = 3
    a = 1
    length = len(data)
    width = len(data[0])
    count1 = 0
    while a < length:
        if data[a][b % width] == '#':
            count1 = count1 + 1
        b = b + 3
        a = a + 1

    return count1


if __name__ == "__main__":
    print(run())
