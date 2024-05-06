import re

def puzzle1():
    with open('data1.txt', 'r') as file:
        s = 0
        lines = file.readlines()
        for line in lines:
            i, j = 0, len(line) - 1
            while line[i] < '0' or line[i] > '9' or line[j] < '0' or line[j] > '9':
                if line[i] >= '0' and line[i] <= '9':
                    j -= 1
                elif line[j] >= '0' and line[j] <= '9':
                    i += 1
                else:
                    i += 1
                    j -= 1
            
            n = line[i] + line[j]
            s += int(n)
        print(s)

def parse(s):
    if s >= '0' and s <= '9':
        return int(s)
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return numbers.index(s) + 1

def puzzle2():
    with open('data1.txt', 'r') as file:
        lines = file.readlines()

        s = 0

        r = 'one|two|three|four|five|six|seven|eight|nine'
        rr = r[::-1]
        r += '|\d'
        rr += '|\d'
        for line in lines:
            first = re.search(r, line)
            second = re.search(rr, line[::-1])
            first, second = parse(first.group()), parse(second.group()[::-1])
            s += (first * 10 + second)
        
        print(s)

if __name__ == '__main__':
    puzzle1()