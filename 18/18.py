from functools import reduce

def parse_input(file):
    lines = open(file).readlines()
    return [l.strip() for l in lines]

def explode_snumber(snumber, i):
    left, right = tuple(snumber[i:].split(']')[0].split(','))
    lenpair = len(left + ',' + right) # number of characters to represent pair
    return add_left(left, snumber[:i-1]) + '0' + add_right(right, snumber[(i + lenpair + 1):])

def add_left(x, snumber_part):
    for i, c in enumerate(snumber_part[::-1]):
        j = len(snumber_part) - i - 1
        if c.isdigit():
            if not(snumber_part[j-1].isdigit()): # explosion into a 1-digit integer
                return snumber_part[:j] + str(int(c) + int(x)) + snumber_part[j+1:]
            else:
                return snumber_part[:j-1] + str(int(snumber_part[j-1] + c) + int(x)) + snumber_part[j+1:]
    return snumber_part
            
def add_right(x, snumber_part):
    for i, c in enumerate(snumber_part):
        if c.isdigit():
            if not snumber_part[i+1].isdigit():
                return snumber_part[:i] + str(int(c) + int(x)) + snumber_part[i+1:]
            else:
                return snumber_part[:i] + str(int(c + snumber_part[i+1]) + int(x)) + snumber_part[i+2:]
    return snumber_part

def reduce_snumber(snumber):
    depth_counter = 0
    for i, c in enumerate(snumber):
        if depth_counter == 5:
            return explode_snumber(snumber, i)
        elif c == '[':
            depth_counter += 1
        elif c == ']':
            depth_counter -= 1
    for i in range(len(snumber)):
        if snumber[i].isdigit() and snumber[i+1].isdigit(): # int > 9
            to_split = int(snumber[i] + snumber[i+1])
            return (
                snumber[:i] + 
                f"[{to_split // 2},{(to_split // 2) + (to_split % 2)}]" + 
                snumber[(i+2):]
            )
    return snumber

def add_snumbers(snum1, snum2):
    last_sum_snumbers = ""
    sum_snumbers = f"[{snum1},{snum2}]"
    while last_sum_snumbers != sum_snumbers:
        last_sum_snumbers = sum_snumbers
        sum_snumbers = reduce_snumber(last_sum_snumbers)
    return sum_snumbers

def magnitude(snumber):
    if isinstance(snumber, int):
        return snumber
    return (3 * magnitude(snumber[0])) + (2 * magnitude(snumber[1]))

if __name__ == "__main__":
    input = parse_input('18/input')
    print("Part 1:", magnitude(eval(reduce(add_snumbers, input))))
    i = 0
    magnitudes = []
    for l1 in input:
        for l2 in input:
            magnitudes += [magnitude(eval(add_snumbers(l1, l2)))]
    print("Part 2:", max(magnitudes))