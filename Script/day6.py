def get_data(in_file):
    with open(in_file) as open_file:
        contents = open_file.read()
    return [int(content) for content in contents.split(',')]


def process_data(data, days):
    print("Initial State: {}".format(data))
    for day in range(days):
        for d in range(len(data)):
            if data[d] == 0:
                data[d] = 6
                data.append(8)
            else:
                data[d] -= 1
        print("After {} Days: Fish - {}".format(day + 1, len(data)))

def dict_process(data, days):
    current_state = {}
    for i in range(9):
        current_state[i] = data.count(i)
    for day in range(days):
        next_state = {}
        for i in range(9):
            if i == 8:
                next_state[i] = current_state[0]
            else:
                next_state[i] = current_state[i + 1]
        if current_state[0] > 0:
            next_state[6] += current_state[0]
        current_state = next_state
        next_state = {}
    total = 0
    for fish in current_state:
        total += current_state[fish]
    print(current_state)
    print(total)


def app():
    #input_file = r'data\test.txt'
    input_file = r'data\real.txt'
    data = get_data(input_file)
    #process_data(data, 256)
    dict_process(data, 256)


if __name__ == '__main__':
    app()