from numpy import median

dict_match = {"{": "}", "(": ")", "[": "]", "<": ">"}
point_table_part1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
point_table_part2 = {")": 1, "]": 2, "}": 3, ">": 4}
openers = set("(<{[")
closers = set(")]}>")

def check_line(line):
    """
    Evaluates the balance of brackets in a given line. It iterates through each
    character, adding openers to a stack and removing closers that match the top
    of the stack. If a mismatch is found, it returns the corresponding penalty
    score from the `point_table_part1` dictionary.

    Args:
        line (str): Described as a string of characters representing a line of
            text to be evaluated for matching brackets.

    Returns:
        int|0: Either the points for a matching bracket sequence or 0 if the
        brackets do not match or are unbalanced.

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
    Generates the corresponding closing bracket sequence for a given input line
    of brackets, using a dictionary mapping brackets to their corresponding closing
    brackets.

    Args:
        line (str): Used to represent a string of characters that may contain
            brackets and other characters.

    Returns:
        str: A string of closing brackets in the reverse order of their corresponding
        opening brackets in the input string.

    """
    bracket_stack = ""
    for c in line:
        bracket_stack = (bracket_stack + c) if c in openers else bracket_stack[:-1]
    closing_stack = ''.join([dict_match[c] for c in bracket_stack])
    return closing_stack[::-1]

def scorer_part_2(closers):
    """
    Calculates a score based on the input `closers`. It multiplies the current
    score by 5 and adds the corresponding value from the `point_table_part2`
    dictionary for each closer in the input list.

    Args:
        closers (List[str]): Used to iterate over a sequence of closing cards.

    Returns:
        int: Calculated as the cumulative product of the initial value 0 and the
        values in the `point_table_part2` dictionary, each multiplied by 5 and
        added to the running total, for each key in the `closers` list.

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
