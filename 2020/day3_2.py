def get_trees(a, b, data):
    length = len(data)
    width = len(data[0])
    x = a
    y = b
    count = 0
    while x < length:
        if data[x][y % width] == '#':
            count = count + 1
        y = y + b
        x = x + a
    return count


def run():
    data = open('input.txt', 'r').read().split('\n')
    return get_trees(1,
                     3,
                     data) * get_trees(2,
                                       1,
                                       data) * get_trees(1,
                                                         5,
                                                         data) * get_trees(1,
                                                                           7,
                                                                           data) * get_trees(1,
                                                                                             1,
                                                                                             data)


if __name__ == "__main__":
    print(run())
