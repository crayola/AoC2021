from numpy import median

dict_match = {"{": "}", "(": ")", "[": "]", "<": ">"}
point_table_part1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
point_table_part2 = {")": 1, "]": 2, "}": 3, ">": 4}
openers = set("(<{[")
closers = set(")]}>")

def check_line(line):
    bracket_stack = ""
    for c in line:
        if c in openers:
            bracket_stack = bracket_stack + c
        else: # c is a closer
            if dict_match[bracket_stack[-1]] == c: # it's the expected closer
                bracket_stack = bracket_stack[:-1]
            else: # error
                return point_table_part1[c]
    return 0
    
def close_line(line):
    bracket_stack = ""
    for c in line:
        bracket_stack = (bracket_stack + c) if c in openers else bracket_stack[:-1]
    closing_stack = ''.join([dict_match[c] for c in bracket_stack])
    return closing_stack[::-1]

def scorer_part_2(closers):
    score = 0
    for c in closers:
        score = score * 5 + point_table_part2[c]
    return score

if __name__ == "__main__":
    lines = [x.strip() for x in open("10/input").readlines()]
    print("Part 1:", sum([check_line(l) for l in lines]))
    good_lines = [l for l in lines if check_line(l) == 0]
    print("Part 2:", median([scorer_part_2(close_line(l)) for l in good_lines]))
