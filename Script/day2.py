from pprint import pprint

def get_data(fn):
    with open(fn) as open_file:
        temp_lines = open_file.readlines()
    return temp_lines
    
def part1(input_lines):
    hor, vert, aim = 0, 0, 0
    for line in input_lines:
        distance = int(line[line.rfind(' ') + 1:])
        if "forward" in line:
            hor += distance
            vert += (distance * aim)
        elif "up" in line:
            aim -= distance
        elif "down" in line:
            aim += distance
        print("Horizontal {} Depth {} Aim {} Total {}".format(hor, vert, aim, hor*vert))
    
def part2(data):
    pass
            

def main():
    file_name = "input.txt"
    data = get_data(file_name)
    part1(data)
    part2(data)

if __name__ == '__main__':
    main()