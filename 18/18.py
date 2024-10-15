from functools import reduce

def parse_input(file):
    """
    Opens a specified file, reads its contents, splits each line into a separate
    element, removes leading/trailing whitespace, and returns a list of these
    cleaned lines.

    Args:
        file (str): Required. It specifies the path to a file containing input
            data to be parsed.

    Returns:
        List[str]: A list of strings, containing each line of the specified file
        after removing leading and trailing whitespace.

    """
    lines = open(file).readlines()
    return [l.strip() for l in lines]

def explode_snumber(snumber, i):
    """
    Separates a pair of numbers within a string, adds a '0' between them, and then
    combines the result with the rest of the string, effectively "exploding" a
    number in a string representation of a Snailfish number.

    Args:
        snumber (str): A string representing a number in a custom format, likely
            a long number split into pairs of digits separated by commas and
            enclosed in square brackets.
        i (int): Used to specify the index within the string `snumber` where the
            explosion of the pair should start.

    Returns:
        str: Formed by concatenating three parts: a prefix from `snumber` before
        the exploded pair, the pair itself with a '0' appended, and a suffix from
        `snumber` after the exploded pair.

    """
    left, right = tuple(snumber[i:].split(']')[0].split(','))
    lenpair = len(left + ',' + right) # number of characters to represent pair
    return add_left(left, snumber[:i-1]) + '0' + add_right(right, snumber[(i + lenpair + 1):])

def add_left(x, snumber_part):
    """
    Adds a given integer `x` to the leftmost non-digit character in a string
    `snumber_part`, propagating the carry to the leftmost digit if necessary.

    Args:
        x (int): Used as an integer value to add to the digit found at the current
            position in the string `snumber_part`.
        snumber_part (str): A sub-string representing a part of a number, where
            the number is assumed to be represented as a string with digits and a
            non-digit character separating each part.

    Returns:
        str: A string that results from adding the integer `x` to the leftmost
        digits of `snumber_part` without carrying over to the next digit if the
        next digit is not a digit.

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
    Adds a given integer `x` to the rightmost digit of a string `snumber_part`
    that is a part of a number. If the next character is also a digit, it adds `x`
    to the sum of the two digits.

    Args:
        x (int): Used to add a value to the digit it is paired with in the string
            `snumber_part`.
        snumber_part (str): Representing a part of a string that contains a number.

    Returns:
        str: The input string `snumber_part` modified by adding the specified
        integer `x` to the rightmost digit that is a valid integer.

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
    Reduces a given string number representation according to a set of rules, which
    include exploding pairs of digits when a depth of 5 is reached and splitting
    pairs of digits when they exceed 9.

    Args:
        snumber (str): Representing a string representation of a number in a
            specific format, likely a nested array of integers, where each element
            is enclosed in square brackets and integers are separated by commas.

    Returns:
        str: Either the modified input string after applying the reduction operation,
        or the same input string if no reduction is needed.

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
    Calculates the sum of two string numbers, represented as a set of strings,
    until the sum stabilizes, indicating the result has no further reduction.

    Args:
        snum1 (str): Representing a single number in string format, likely a string
            representation of an integer or a sequence of digits.
        snum2 (str): Represented as the second number in a string of two numbers
            separated by a comma, for example, "123,456".

    Returns:
        str: The result of repeatedly applying the `reduce_snumber` function to
        the initial sum of the two input strings until no further reduction is possible.

    """
    last_sum_snumbers = ""
    sum_snumbers = f"[{snum1},{snum2}]"
    while last_sum_snumbers != sum_snumbers:
        last_sum_snumbers = sum_snumbers
        sum_snumbers = reduce_snumber(last_sum_snumbers)
    return sum_snumbers

def magnitude(snumber):
    """
    Calculates the magnitude of a given number, where the magnitude of an integer
    is its value, and the magnitude of a string is calculated recursively based
    on the magnitude of its digits, with each digit's magnitude being three times
    the magnitude of the first digit and two times the magnitude of the second digit.

    Args:
        snumber (str | List[str]): Expected to represent a binary number in string
            or list of string format.

    Returns:
        int: A base-10 magnitude of the given number, calculated recursively
        according to the given formula.

    """
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