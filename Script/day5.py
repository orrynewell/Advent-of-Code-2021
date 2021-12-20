def get_data(in_file):
    data_list = []
    with open(in_file) as input_file:
        raw_data = input_file.readlines()
    processed_data = [r.replace('\n', '') for r in raw_data]
    for p in processed_data:
        cord1 = p[:p.find(' ')].strip()
        xcord1 = int(cord1[:cord1.find(',')])
        ycord1 = int(cord1[cord1.find(',') + 1:])
        cord2 = p[p.rfind(' '):].strip()
        xcord2 = int(cord2[:cord2.find(',')])
        ycord2 = int(cord2[cord2.find(',') + 1:])
        data_list.append([xcord1, ycord1, xcord2, ycord2])
    return data_list


def part1(dl, range_num):
    raw_data = []
    for i in range(range_num):
        raw_data.append([])
        for j in range(range_num):
            raw_data[i].append(0)
    for d in dl:
        # part 1
        if d[0] == d[2]:
            for i in range(abs(d[1] - d[3]) + 1):
                raw_data[max(d[1], d[3]) - i][d[0]] += 1
        elif d[1] == d[3]:
            for i in range(abs(d[0] - d[2]) + 1):
                raw_data[d[1]][max(d[0], d[2]) - i] += 1
        # part 2 - adds diags
        else:
            if d[0] > d[2]:
                x_mov = -1
            else:
                x_mov = 1
            if d[1] > d[3]:
                y_mov = -1
            else:
                y_mov = 1
            for i in range(abs(d[0] - d[2]) + 1):
                raw_data[d[1] + (y_mov * i)][d[0] + (x_mov * i)] += 1
    count = 0
    for i in range(range_num):
        for j in range(range_num):
            if raw_data[i][j] > 1:
                count += 1
        print("{}".format(raw_data[i]))
    print(count)


def app():
    input_file = r'data\real.txt'
    dl = get_data(input_file)
    part1(dl, 1000)


if __name__ == '__main__':
    app()
