import math

def read_data():
    directions = ''
    graph = {}

    with open('data8.txt', 'r') as file:
        lines = file.readlines()
        directions = lines[0].strip()

        for line in lines[2:]:
            l = line.strip().split(' = ')
            l[1] = l[1][1:-1].split(', ')
            graph[l[0]] = l[1]
    
    return directions, graph

def puzzle1():
    directions, graph = read_data()

    curr, end = 'AAA', 'ZZZ'
    steps = 0
    dir_index = 0

    while curr != end:
        curr = graph[curr][0 if directions[dir_index] == 'L' else 1]
        steps += 1
        dir_index = (dir_index + 1) % len(directions)
    
    print(steps)

def puzzle2():
    directions, graph = read_data()

    starting_positions = [key for key in graph if key.endswith('A')]

    steps = []

    for node in starting_positions:
        curr = node
        step_count, dir_index = 0, 0

        while not curr.endswith('Z'):
            curr = graph[curr][0 if directions[dir_index] == 'L' else 1]
            step_count += 1
            dir_index = (dir_index + 1) % len(directions)
        
        steps.append(step_count)
    
    lcm = math.lcm(*steps)

    print(lcm)

if __name__ == '__main__':
    puzzle2()
