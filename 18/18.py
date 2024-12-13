from functools import reduce

def parse_input(file):
    lines = open(file).readlines()
    return [l.strip() for l in lines]

def explode_snumber(snumber, i):
    left, right = tuple(snumber[i:].split(']')[0].split(','))
    lenpair = len(left + ',' + right) # number of characters to represent pair
    return add_left(left, snumber[:i-1]) + '0' + add_right(right, snumber[(i + lenpair + 1):])

def add_left(x, snumber_part):
    """
    Adds a given integer `x` to the leftmost digit of a string `snumber_part` that
    represents a number in a specific format, propagating the carry to the next
    digit if necessary.

    Args:
        x (int): Used to add to the digit at the specified position in the
            `snumber_part` string.
        snumber_part (str): Expected to be a part of a number, typically a string
            containing digits and possibly a non-digit character at the left end.

    Returns:
        str: Modified string with the given integer value `x` added to the leftmost
        digit of the string `snumber_part` that is a digit.

    """
    for i, c in enumerate(snumber_part[::-1]):
        j = len(snumber_part) - i - 1
        if c.isdigit():
            if not(snumber_part[j-1].isdigit()): # explosion into a 1-digit integer
                return snumber_part[:j] + str(int(c) + int(x)) + snumber_part[j+1:]
            else:
                return snumber_part[:j-1] + str(int(snumber_part[j-1] + c) + int(x)) + snumber_part[j+1:]
    return snumber_part
            
def add_right(x, snumber_part):
    """
    Adds a given number to the rightmost digit of a string that represents a number,
    where the rightmost digit is part of a multi-digit number. It then returns the
    modified string.

    Args:
        x (int): Used to add its value to the digit in the string `snumber_part`
            at the specified position.
        snumber_part (str): Expected to be a part of a string that represents a
            number, with at least one digit.

    Returns:
        str: Modified string where the rightmost digits are added to `x`.

    """
    for i, c in enumerate(snumber_part):
        if c.isdigit():
            if not snumber_part[i+1].isdigit():
                return snumber_part[:i] + str(int(c) + int(x)) + snumber_part[i+1:]
            else:
                return snumber_part[:i] + str(int(c + snumber_part[i+1]) + int(x)) + snumber_part[i+2:]
    return snumber_part

def reduce_snumber(snumber):
    """
    Reduces a given S-number by either exploding it when its depth reaches 5 or
    splitting it when it contains two consecutive digits.

    Args:
        snumber (str): Expected to be a string representation of a number in a
            custom format, specifically a nested string of integers and square brackets.

    Returns:
        str: Either the original input string `snumber` if it cannot be reduced
        further, or a reduced version of `snumber` after applying the rules of
        addition of two numbers in a snumber (nested list of integers) by either
        exploding it when the depth of brackets reaches 5 or splitting it when two
        numbers are adjacent.

    """
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
    """
    Computes the sum of two string numbers, represented as a list of digits, by
    repeatedly applying the `reduce_snumber` function until the result no longer
    changes.

    Args:
        snum1 (str): Used as a string representation of a number in the process
            of adding two numbers represented as strings.
        snum2 (str): Represented as a string that denotes a number, likely a set
            number, which is a number represented in a specific format or notation,
            possibly as a string of digits or characters.

    Returns:
        str: The result of the sum of two strings representing sets of numbers,
        where each number in the set is represented as a string.

    """
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