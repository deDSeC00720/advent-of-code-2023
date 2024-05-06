def puzzle1():
    with open('data2.txt', 'r') as file:

        s = 0

        for line in file.readlines():
            colon_split = line.split(':')
            game_no = int(colon_split[0].split(' ')[1])
            colon_split[1] = colon_split[1].strip()
            reveals = colon_split[1].split(';')
            reveals = [r.strip() for r in reveals]
            possible = True
            for r in reveals:
                reveal_split = r.split(',')
                reveal_split = [rs.strip() for rs in reveal_split]
                cube_and_color = [rs.split(' ') for rs in reveal_split]

                for i in cube_and_color:
                    if i[1] == 'red' and int(i[0]) > 12:
                        possible = False
                        break
                    if i[1] == 'green' and int(i[0]) > 13:
                        possible = False
                        break
                    if i[1] == 'blue' and int(i[0]) > 14:
                        possible = False
                        break
                if not possible:
                    break
            
            if possible:
                s += game_no

        print(s)

def puzzle2():
    with open('data2.txt', 'r') as file:
        s = 0

        for line in file.readlines():
            maxred = 0
            maxgreen = 0
            maxblue = 0
            colon_split = line.split(':')
            colon_split[1] = colon_split[1].strip()
            reveals = colon_split[1].split(';')
            reveals = [r.strip() for r in reveals]
            for r in reveals:
                reveal_split = r.split(',')
                reveal_split = [rs.strip() for rs in reveal_split]
                cube_and_color = [rs.split(' ') for rs in reveal_split]

                for i in cube_and_color:
                    if i[1] == 'red':
                        maxred = maxred if maxred >= int(i[0]) else int(i[0])
                    if i[1] == 'green':
                        maxgreen = maxgreen if maxgreen >= int(i[0]) else int(i[0])
                    if i[1] == 'blue':
                        maxblue = maxblue if maxblue >= int(i[0]) else int(i[0])
            
            prod = maxred * maxgreen * maxblue
            s += prod

        print(s)

if __name__ == '__main__':
    puzzle2()