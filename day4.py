def puzzle1():
    with open('data4.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split(':')[1] for line in lines]

        s = 0

        for line in lines:
            split = line.split('|')
            winning_num = split[0].split(' ')
            nums = split[1].split(' ')
            winning_num = list(filter(lambda x: x != '', winning_num))
            nums = list(filter(lambda x: x != '', nums))
            set1 = set(winning_num)
            set2 = set(nums)
            intersection = set1 & set2
            s += 2 ** (len(intersection) - 1) if len(intersection) != 0 else 0
        
    print(s)


def puzzle2():
    def get_num_of_matching_numbers(s: str):
        split = s.split('|')
        win = set(filter(lambda x: x != '', split[0].split(' ')))
        nums = set(filter(lambda x: x != '', split[1].split(' ')))

        return len(win & nums)


    with open('data4.txt', 'r') as file:
        lines = file.readlines()
        lines = [i.strip().split(':')[1].strip() for i in lines]

        indices = [i for i, _ in enumerate(lines)]
        mapp = {}

        for i in indices:
            n = get_num_of_matching_numbers(lines[i])
            factor = mapp[i] + 1 if i in mapp else 1
            for j in range(1, n + 1):
                mapp[i + j] = mapp[i + j] + factor if i + j in mapp else factor
        
        total = len(indices)
        for key in mapp:
            total += mapp[key]
        print(total)
        

    pass

if __name__ == '__main__':
    puzzle2()