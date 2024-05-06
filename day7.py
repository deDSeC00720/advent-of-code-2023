strength_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
strength_order_modified = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def read_data():
    cards = []

    with open('data7.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            cards.append(line.strip().split(' '))
    
    return cards

def compare_card(c1, c2, strength):
    for i in range(0, len(c1)):
        if strength.index(c1[i]) == strength.index(c2[i]):
            continue
        return True if strength.index(c1[i]) < strength.index(c2[i]) else False

    return True

def get_kind_index(card, processJ):
    char_count = {}
    for c in card:
        char_count[c] = char_count.get(c, 0) + 1
    
    if len(char_count) == 1:
        return 6
    
    if len(char_count) == 2:
        return 6 if processJ and 'J' in char_count else 5 if 4 in char_count.values() else 4
    
    if len(char_count) == 3:
        if 3 in char_count.values():
            return 5 if processJ and 'J' in char_count else 3
        
        return (5 if char_count['J'] == 2 else 4) if processJ and 'J' in char_count else 2
    
    if len(char_count) == 4:
        return 3 if processJ and 'J' in char_count else 1
    
    if len(char_count) == 5:
        return 1 if processJ and 'J' in char_count else 0

def get_winnings(strength_order_arr, processJ):
    cards = read_data()

    kinds = [[], [], [], [], [], [], []]

    for card in cards:
        kind_index = get_kind_index(card[0], processJ)

        added = False
        for i, k in enumerate(kinds[kind_index]):
            if compare_card(card[0], k[0], strength_order_arr):
                kinds[kind_index].insert(i, card)
                added = True
                break
        if not added:
            kinds[kind_index].append(card)
    
    count = 1
    output = 0

    for kind in kinds:
        for card in kind:
            output += count * int(card[1])
            count += 1
    
    return output

def puzzle1():
    print(get_winnings(strength_order, False))

def puzzle2():
    print(get_winnings(strength_order_modified, True))

if __name__ == '__main__':
    puzzle2()