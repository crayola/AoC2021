import numpy as np

def parse_input(file):
    lines = open(file).readlines()
    lines = [x.strip() for x in lines]
    return lines

dict_match = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
}
openers = set("(<{[")
closers = set(")]}>")
point_table = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
point_table_2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def check_line(line):
    bracket_stack = ""
    for c in line:
        if c in openers:
            bracket_stack = bracket_stack + c
        if c in closers:
            if c in closers and dict_match[bracket_stack[-1]] == c:
                bracket_stack = bracket_stack[:-1]
            else:
                return point_table[c]
    return 0
    


def close_line(line):
    bracket_stack = ""
    for c in line:
        if c in openers:
            bracket_stack = bracket_stack + c
        else: 
            bracket_stack = bracket_stack[:-1]
    closing_stack = ''.join([dict_match[c] for c in bracket_stack])
    return closing_stack[::-1]

def scorer_part_2(closers):
    score = 0
    for c in closers:
        score = score * 5
        score += point_table_2[c]
    return score



if __name__ == "__main__":
    lines = parse_input("10/input")
    print("Part 1:", sum([check_line(l) for l in lines]))
    good_lines = [l for l in lines if check_line(l) == 0]
    print("Part 2:", np.median([scorer_part_2(close_line(l)) for l in good_lines]))
    #print("Part 1:", sum([check_line(l) for l in lines]))
