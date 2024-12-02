from pathlib import Path


def read_input(file_path: Path)->list:
    read_data = file_path.read_text()
    left_side = []
    right_side = []
    for line in read_data.split('\n'):
        _line = line.split()
        left_side.append(_line[0].strip())
        right_side.append(_line[1].strip())
    result = [left_side,right_side]
    return result



def get_distance_between_numbers(left_side:list,right_side:list)->list:
    left_side.sort()
    right_side.sort()

    result = list(map(lambda x: abs(int(x[0])-int(x[1])), zip(left_side,right_side)))

    return result

if __name__ == '__main__':
    data = read_input(Path('inputs/day1_inputs'))
    day1_result = how_far_apart(*data)
    print(sum(day1_result))