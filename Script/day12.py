import os
import datetime as dt
from pprint import pprint as pp


def get_data(text):
    file = open(text)
    contents = file.read()
    content_list = contents.splitlines()
    direction_dict = {}
    for content in content_list:
        start_pos = content[:content.find('-')]
        end_pos = content[content.find('-') + 1:]
        if start_pos not in direction_dict.keys():
            direction_dict[start_pos] = [end_pos]
            if end_pos not in ['start', 'end'] and start_pos not in ['start', 'end']:
                if end_pos not in direction_dict.keys():
                    direction_dict[end_pos] = [start_pos]
                else:
                    direction_dict[end_pos].append(start_pos)
        else:
            direction_dict[start_pos].append(end_pos)
            if end_pos not in ['start', 'end'] and start_pos not in ['start', 'end']:
                if end_pos not in direction_dict.keys():
                    direction_dict[end_pos] = [start_pos]
                else:
                    direction_dict[end_pos].append(start_pos)
    return direction_dict


def process_data(direction_dict):
    possible_paths = []
    pos = "start"
    options = direction_dict[pos]
    current_path = ['start']
    while True:
        if options:
            for option in options:
                try:
                    print("Current Position: {}".format(option))
                    if option.islower():
                        print("Trying to remove {} from {} - {}".format(option, pos, direction_dict[pos]))
                        direction_dict[pos].remove(option)
                    pos = option
                    current_path.append(option)
                    if pos == 'end':
                        print("Success")
                        possible_paths.append(current_path)
                    options = direction_dict[option]
                except KeyError:
                    print("Out Of Path, Failure")
                break
            print("location {} -  path so far {}".format(pos, current_path))
        else:
            break
    print(possible_paths)

def app():
    test_data = r'data\test.txt'
    direction_dict = get_data(test_data)
    process_data(direction_dict)



if __name__ == '__main__':
    start_time = dt.datetime.now()
    print("Start: {}".format(start_time))
    app()
    end_time = dt.datetime.now()
    print("End: {}\nElapsed: {}".format(end_time, end_time - start_time))