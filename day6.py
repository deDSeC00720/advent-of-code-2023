from functools import reduce

def read_data():
    time = []
    distance = []
    with open('data6.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            if time:
                distance = list(map(lambda x: int(x), line.split(':')[1].strip().split()))
            else:
                time = list(map(lambda x: int(x), line.split(':')[1].strip().split()))
    
    return [[time[i], distance[i]] for i in range(0, len(time))]

def no_of_ways(time, dist):
    mid = time // 2
    max_dist = mid * (time - mid)
    ways = 0

    if max_dist > dist:
        ways = 1
        while max_dist > dist and mid > 0:
            mid -= 1
            max_dist = mid * (time - mid)
            ways += 1 if max_dist > dist else 0
        
        ways *= 2
        if time % 2 == 0:
            ways -= 1
    
    return ways

def puzzle1():
    data = read_data()
    output = 1

    for d in data:
        output *= no_of_ways(d[0], d[1])
    
    print(output)

def puzzle2():
    data = read_data()

    time, dist = reduce(lambda acc, curr: [int(str(acc[0]) + str(curr[0])), int(str(acc[1]) + str(curr[1]))], data, ['', ''])

    print(no_of_ways(time, dist))

if __name__ == '__main__':
    puzzle2()