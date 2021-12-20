from pprint import pprint

def get_data(fn):
    with open(fn) as open_file:
        temp_lines = open_file.readlines()
    input_lines = [int(line) for line in temp_lines]
    return input_lines
    
def part1(input_lines):
    count = 0
    local_max = input_lines[0]
    for i in input_lines[1:]:
        if i > local_max:
            count+=1
        local_max = i
    print(count)
    
def part2(data):
    count = 0
    i = 1
    list_list = [[data[0], data[1], data[2]], [data[1], data[2]], [data[2]]]
    running_max = sum(list_list[0])
    for d in data[3:]:
        i += 1
        for l in range(len(list_list)):
            if len(list_list[l]) == 3:
                local_max = sum(list_list[l])
                list_list[l] = []
                if local_max > running_max:
                    count += 1
                running_max = local_max
            list_list[l].append(d)
    for l in range(len(list_list)):
            if len(list_list[l]) == 3:
                local_max = sum(list_list[l])
                list_list[l] = []
                if local_max > running_max:
                    count += 1
    print(count)
            

def main():
    file_name = "input.txt"
    data = get_data(file_name)
    #part1(data)
    part2(data)

if __name__ == '__main__':
    main()