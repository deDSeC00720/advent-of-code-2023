def read_data():
    data = []
    with open('data9.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            data.append([int(i) for i in line.strip().split(' ')])
    
    return data

def all_zeroes(arr):
    for val in arr:
        if val != 0:
            return False
    return True

def extrapolate(data, next_value=True):
    levels = [data]
    index = 0

    while not all_zeroes(levels[index]):
        new_level = []
        for i in range(1, len(levels[index])):
            diff = levels[index][i] - levels[index][i - 1]
            new_level.append(diff)
        levels.append(new_level)
        index += 1

    s = 0
    for i in range(len(levels) - 2, -1, -1):
        s = levels[i][-1 if next_value else 0] + (1 if next_value else -1) * (s)

        if next_value:
            s = levels[i][-1] + s
            s += levels[i][-1]
        else:
            s = levels[i][0] - s
    return s
    


def puzzle1():
    data = read_data()
    output = 0
    for row in data:
        output += extrapolate(row)
    
    print(output)

def puzzle2():
    data = read_data()
    output = 0
    for row in data:
        output += extrapolate(row, False)
    
    print(output)


if __name__ == '__main__':
    puzzle2()