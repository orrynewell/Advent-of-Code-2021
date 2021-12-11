"""
Advent of Code - Day 11 - Dumbo Octopus
Link to Description - https://adventofcode.com/2021/day/11
"""
import os
import datetime as dt


def parse_data(starting_data, list_size):
    """
    Parses the data from a string into a list of list
    :param starting_data: The starting data string
    :param list_size: the size of the list
    :return: A list of list for processing
    """
    return_list = []
    short_list = []
    for i in range(len(starting_data)):
        short_list.append(int(starting_data[i]))
        if (i+1) % list_size == 0:
            return_list.append(short_list)
            short_list = []
    print_data(return_list, list_size, "Starting Data", 0)
    return return_list


def print_data(data, list_size, title, flashes):
    """
    Print Data - Quality of life function for checking outputs
    :param data: The list of list
    :param list_size: The size of the list
    :param title: What to call the print out
    :param flashes: Number of flahses
    :return:
    """
    if type(title) == int:
        print("Loop {} | Flashes - {}".format(title, flashes))
    else:
        print("{}".format(title))
    print("-" * (list_size * 2))
    for i in range(list_size):
        print(' '.join([str(elem) for elem in data[i]]))
    print("-" * (list_size * 2))


def process_data(data, list_size, loops):
    """
    Process Data - Loops through the data and ups all items by 1 initially, breaks when syn happens
    :param data: The list of list
    :param list_size: Number of items in the list
    :param loops: THe number of loops
    :return: Nothing
    """
    flashes = 0
    for loop in range(loops):
        black_list = []
        for i in range(list_size):
            for j in range(list_size):
                if data[i][j] < 9:
                    data[i][j] += 1
                else:
                    flashes += 1
                    data[i][j] = 0
        for i in range(list_size):
            for j in range(list_size):
                if data[i][j] == 0:
                    data, flashes = flash(i, j, data, black_list, flashes)
        print_data(data, list_size, loop+1, flashes)
        if check_snc(data):
            print("Synchronization has occurred at loop {}".format(loop + 1))
            os._exit(1)


def flash(cord1, cord2, data, black_list, flashes):
    """
    Flash - When a value is greater than 9 is process
    This function is recursive and is called when an additional item above 9 is activated
    :param cord1: x coordinate
    :param cord2: y coordinate
    :param data: The list of list
    :param black_list: The items to not process a second time
    :param flashes: The number of flashes
    :return: flashes and data
    """
    if [cord1, cord2] not in black_list:
        black_list.append([cord1, cord2])
        for l in cord_circle:
            n_cord1 = cord1 + l[0]
            n_cord2 = cord2 + l[1]
            if (n_cord1 not in [-1, list_size]) and (n_cord2 not in [-1, list_size]) and [n_cord1, n_cord2] not in black_list:
                if data[n_cord1][n_cord2] < 9 and data[n_cord1][n_cord2] != 0:
                    data[n_cord1][n_cord2] += 1
                elif data[n_cord1][n_cord2] == 0:
                    pass
                else:
                    flashes += 1
                    data[n_cord1][n_cord2] = 0
                    data, flashes = flash(n_cord1, n_cord2, data, black_list, flashes)
    return data, flashes


def check_snc(data):
    """
    Check Syn - Checks for when all items are zero
    :param data: The list of list
    :return: True when it is synchronized
    """
    for i in range(list_size):
        for j in range(list_size):
            if data[i][j] == 0:
                pass
            else:
                return False
    return True


def app():
    """
    App - Runs the accompanying functions
    :return: Nothing
    """
    starting_data = "4525436417" \
                    "1851242553" \
                    "5421435521" \
                    "8431325447" \
                    "4517438332" \
                    "3521262111" \
                    "3331541734" \
                    "4351836641" \
                    "2753881442" \
                    "7717616863"
    parsed_data = parse_data(starting_data, list_size)
    # Could have changed the looping to a while statement
    process_data(parsed_data, list_size, 1000)


if __name__ == '__main__':
    """
    Main runner
    """
    start_time = dt.datetime.now()
    list_size = 10
    # Cordinate list for checking each item touching the one that is activated.
    cord_circle = [[-1, -1],
                   [-1, 0],
                   [-1, 1],
                   [0, -1],
                   [0, 1],
                   [1, -1],
                   [1, 0],
                   [1, 1]]
    print("Start - {}".format(start_time))
    app()
    print("End - {}\nElapsed Time - {}".format(dt.datetime.now(), (dt.datetime.now() - start_time)))
