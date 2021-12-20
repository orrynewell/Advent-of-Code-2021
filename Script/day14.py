def get_input_data(fp):
    out_dict = {}
    with open(fp) as file:
        data = file.read().splitlines()
    for i in range(len(data)):
        if i == 0:
            out_dict["process_line"] = data[i]
        elif i > 1:
            out_dict[data[i][0:2]] = data[i][6:]
    return out_dict

    
def process_data(data, loops):
    process_line = data['process_line']
    new_line = data['process_line'][0]
    for l in range(loops):
        print("Loop {}".format(l + 1))
        for i in range(0, len(process_line), 1):
            sub_string = process_line[i: i+2]
            if len(sub_string) > 1:
                add_line = data[sub_string] + sub_string[1:]
                new_line += add_line
        if l == loops - 1:
            get_counts(l, new_line)
            return
        process_line = new_line
        new_line = process_line[0]


def get_counts(l, line):
    count_list = []
    for i in list(set(line)):
        count_list.append(line.count(i))
    difference = max(count_list) - min(count_list)
    print("The difference after {} loops is {}".format(l + 1, difference))


def main():
    file_path = r"data\real.txt"
    data = get_input_data(file_path)
    process_data(data, 40)


if __name__ == '__main__':
    main()