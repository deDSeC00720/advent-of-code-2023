import sys

def read_data():
    seeds = []
    data = []

    with open('data5.txt', 'r') as file:
        lines = file.readlines()

        seeds = list(map(lambda x: int(x), lines[0].split(':')[1].strip().split(' ')))

        for i in range(1, len(lines)):
            if lines[i].startswith('\n'):
                continue

            if lines[i].startswith('seed-to-soil') or lines[i].startswith('soil-to-fertilizer') or lines[i].startswith('fertilizer-to-water') or lines[i].startswith('water-to-light') or lines[i].startswith('light-to-temperature') or lines[i].startswith('temperature-to-humidity') or lines[i].startswith('humidity-to-location'):
                data.append([])
                continue

            data[-1].append(list(map(lambda x: int(x), lines[i].strip().split(' '))))
    
    return [seeds, data]

def puzzle1():
    seeds, data = read_data()

    min_location_seed = sys.maxsize

    for seed in seeds:
        k = seed
        for i in data:
            for j in i:
                if j[1] <= k and k <= j[1] + j[2] - 1:
                    k = j[0] + (k - j[1])
                    break
        
        min_location_seed = min([min_location_seed, k])
        
    print(min_location_seed)

def process_range(next_range, map_range):
    processed = []
    unprocessed = []
    for i in range(0, len(next_range), 2):
        start = next_range[i]
        length = next_range[i + 1]

        if start >= map_range[1] + map_range[2] or start + length - 1 < map_range[1]:
            unprocessed.extend([start, length])
            continue

        if start >= map_range[1] and start + length <= map_range[1] + map_range[2]:
            processed.extend([map_range[0] + start - map_range[1], length])
            continue

        if start >= map_range[1]:
            processed.extend([map_range[0] + start - map_range[1], map_range[1] + map_range[2] - start])
            unprocessed.extend([map_range[1] + map_range[2], start + length - map_range[1] - map_range[2]])
            continue

        if start + length - 1 < map_range[1] + map_range[2]:
            processed.extend([map_range[0], start + length - map_range[1]])
            unprocessed.extend([start, map_range[1] - start])
            continue

        unprocessed.extend([start, map_range[1] - start, map_range[1] + map_range[2], start + length - map_range[1] - map_range[2]])
        processed.extend([map_range[0], map_range[2]])
    
    return processed, unprocessed


def puzzle2():
    seeds, data = read_data()

    min_location = []

    for i in range(0, len(seeds), 2):
        next_range = [seeds[i], seeds[i + 1]]
        for j in data:
            processed_range = []
            unprocessed_range = next_range
            for k in j:
                range1, unprocessed_range = process_range(unprocessed_range, k)
                processed_range.extend(range1)
                if len(unprocessed_range) == 0:
                    break
            
            next_range = processed_range + unprocessed_range

        min_location.append(min(map(lambda x: x[1], filter(lambda x: x[0] % 2 == 0, enumerate(next_range)))))

    
    answer = min(min_location)

    print(answer)

if __name__ == '__main__':
    puzzle2()
