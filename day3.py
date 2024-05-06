def puzzle1():
    with open('data3.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        s = 0

        def is_symbol(ch):
            return True if (ch < '0' or ch > '9') and ch != '.' else False

        def is_part_number(i, l, r):
            len_of_line = len(lines[i])
            for j in range(l, r + 1):
                if i - 1 >= 0:
                    if j == l and j - 1 >= 0 and is_symbol(lines[i - 1][j - 1]):
                        if l == 138:
                            print('above')
                        return True
                    if is_symbol(lines[i - 1][j]):
                        if l == 138:
                            print('just above')
                        return True
                    if j == r and j + 1 < len_of_line and is_symbol(lines[i - 1][j + 1]):
                        if l == 138:
                            print('above right')
                        return True
                if j == l and j - 1 >= 0 and is_symbol(lines[i][j - 1]):
                    if l == 138:
                        print('left')
                    return True
                if j == r and j + 1 < len_of_line and is_symbol(lines[i][j + 1]):
                    if l == 138:
                        print('right')
                    return True
                if i + 1 < len(lines):
                    if j == l and j - 1 >= 0 and is_symbol(lines[i + 1][j - 1]):
                        if l == 138:
                            print('below')
                        return True
                    if is_symbol(lines[i + 1][j]):
                        if l == 138:
                            print('just below')
                        return True
                    if j == r and j + 1 < len_of_line and is_symbol(lines[i + 1][j + 1]):
                        if l == 138:
                            print('below right')
                        return True
            return False

        for i, line in enumerate(lines):
            start, end = -1, -1
            for j, ch in enumerate(line):
                if ch >= '0' and ch <= '9':
                    if start == -1:
                        start = j
                        end = j
                    else:
                        end = j
                else:
                    if start == -1:
                        continue
                    if is_part_number(i, start, end):
                        s += int(line[start:end + 1])
                    start, end = -1, -1
                
                if end == len(line) - 1:
                    if is_part_number(i, start, end):
                        s += int(line[start: end + 1])

        print(s)

def puzzle2():
    with open('data3.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

        def extract_num_range(i, j):
            r = [i]
            k = j
            while j - 1 >= 0 and lines[i][j - 1] >= '0' and lines[i][j - 1] <= '9':
                j -= 1
            while k + 1 < len(lines[i]) and lines[i][k + 1] >= '0' and lines[i][k + 1] <= '9':
                k += 1
            
            r.append(j)
            r.append(k)
            return r

        def find_num(i, j):
            i_start = i if i == 0 else i - 1
            i_end = i if i + 1 == len(lines) else i + 1
            j_start = j if j == 0 else j - 1
            j_end = j if j == len(lines[i]) - 1 else j + 1

            range1, range2 = None, None

            for k in range(i_start, i_end + 1):
                for l in range(j_start, j_end + 1):
                    if lines[k][l] >= '0' and lines[k][l] <= '9':
                        if range1:
                            if range1[0] == k and l >= range1[1] and l <= range1[2]:
                                continue
                            range2 = extract_num_range(k, l)
                            return range1, range2
                        
                        range1 = extract_num_range(k, l)
            
            return range1, range2
        
        s = 0

        for i, line in enumerate(lines):
            for j, ch in enumerate(line):
                if ch == '*':
                    range1, range2 = find_num(i, j)
                    if range1 and range2:
                        print(range1, range2)
                        s += int(lines[range1[0]][range1[1]:range1[2] + 1]) * int(lines[range2[0]][range2[1]:range2[2] + 1])

    print(s)


if __name__ == '__main__':
    puzzle2()