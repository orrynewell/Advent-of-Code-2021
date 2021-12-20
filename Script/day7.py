import numpy


def get_data(in_file):
    with open(in_file) as open_file:
        contents = open_file.read()
    return [int(content) for content in contents.split(',')]


def part1(data):
    median = int(numpy.median(data))
    fuel_cost = 0
    for d in data:
        fuel_cost += abs(d - median)
    print(fuel_cost)


def part2(data):
    fuel_cost = 0
    mean = int(numpy.mean(data))
    print(mean)
    for d in data:
        fuel_cost += sum([i for i in range(1, abs(d - mean) + 1)])
    print(fuel_cost)


def app():
    #input_file = r'data\test.txt'
    input_file = r'data\real.txt'
    data = get_data(input_file)
    #part1(data)
    part2(data)


if __name__ == '__main__':
    app()