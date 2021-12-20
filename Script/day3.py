from pprint import pprint

def get_data(fn):
    with open(fn) as open_file:
        temp_lines = open_file.readlines()
    temp_lines = [temp.replace('\n', '') for temp in temp_lines]
    return temp_lines
    
def part1(input_lines):
    print(len(input_lines[0]))
    gamma, epilson = '', ''
    for s in range(len(input_lines[0])):
        common_dict = {'1': 0,
                       '0': 0}
        for i in input_lines:
            if i[s] == '1':
                common_dict['1'] += 1
            else:
                common_dict['0'] += 1
        if common_dict['1'] > common_dict['0']:
            gamma += '1'
            epilson += '0'
        else:
            gamma += '0'
            epilson += '1'
        print("Gamma - {}, Epilson = {}".format(gamma, epilson))
    decimal_gamma = binary_to_decimal(gamma)
    decimal_epilson = binary_to_decimal(epilson)
    print("Result - {}".format(decimal_gamma * decimal_epilson))
    
def binary_to_decimal(binary):
    return int(binary, 2)
    
def part2(data):
    count = 0
    data_reset = data
    while True:
        if len(data) == 1:
            break
        data_dict = {'1': [],
                     '0': []}
        for d in data:
            if d[count] == '1':
                data_dict['1'].append(d)
            else:
                data_dict['0'].append(d)
        if len(data_dict['1']) >= len(data_dict['0']):
            data = data_dict['1']
            binary = data
        else:
            data = data_dict['0']
            binary = data
        count += 1
    co2 = binary_to_decimal(binary[0])
    print("High: {} - {}".format(binary[0], binary_to_decimal(binary[0])))
    count = 0
    data = data_reset
    while True:
        if len(data) == 1:
            break
        data_dict = {'1': [],
                     '0': []}
        for d in data:
            if d[count] == '1':
                data_dict['1'].append(d)
            else:
                data_dict['0'].append(d)
        if len(data_dict['1']) < len(data_dict['0']):
            data = data_dict['1']
            binary = data
        else:
            data = data_dict['0']
            binary = data
        count += 1
    o2 = binary_to_decimal(binary[0])
    print("Low: {} - {}".format(binary[0], binary_to_decimal(binary[0])))
    print("Total: {}".format(co2 * o2))
            

def main():
    file_name = "input.txt"
    data = get_data(file_name)
    #part1(data)
    part2(data)

if __name__ == '__main__':
    main()