from numpy import median

dict_match = {"{": "}", "(": ")", "[": "]", "<": ">"}
point_table_part1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
point_table_part2 = {")": 1, "]": 2, "}": 3, ">": 4}
openers = set("(<{[")
closers = set(")]}>")

def check_line(line):
    """
    Evaluates the balance of brackets in a given line of code. It uses a stack to
    track opening brackets and matches them with closing brackets, returning the
    corresponding score from a predefined table when a mismatch is found.

    Args:
        line (str): Representing a line of text, presumably containing brackets
            or other characters to be checked for matching.

    Returns:
        int|0: A score from the `point_table_part1` dictionary, representing the
        points earned for a line of code, or 0 if the line is valid.

    """
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
    """
    Matches opening brackets in a given line with their corresponding closing
    brackets, returning the closing brackets in the reverse order of their opening
    counterparts.

    Args:
        line (str): Representing a string of characters that may contain opening
            and closing brackets.

    Returns:
        str: The string of closing brackets that would match the opening brackets
        in the input string when read from right to left.

    """
    bracket_stack = ""
    for c in line:
        bracket_stack = (bracket_stack + c) if c in openers else bracket_stack[:-1]
    closing_stack = ''.join([dict_match[c] for c in bracket_stack])
    return closing_stack[::-1]

def scorer_part_2(closers):
    """
    Calculates a score based on a sequence of closers. It multiplies the current
    score by 5 and adds the value from a point table corresponding to the current
    closer, iterating through the sequence of closers.

    Args:
        closers (List[str]): Iterated over to access the elements of a predefined
            point table.

    Returns:
        int: The cumulative score calculated by multiplying the previous score by
        5 and adding the point value from the `point_table_part2` dictionary
        corresponding to each character in the `closers` string.

    """
    score = 0
    for c in closers:
        score = score * 5 + point_table_part2[c]
    return score

if __name__ == "__main__":
    lines = [x.strip() for x in open("10/input").readlines()]
    print("Part 1:", sum([check_line(l) for l in lines]))
    good_lines = [l for l in lines if check_line(l) == 0]
    print("Part 2:", median([scorer_part_2(close_line(l)) for l in good_lines]))
