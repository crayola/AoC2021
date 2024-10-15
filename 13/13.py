import numpy as np

def fold_point(instruction, coordinates):
    """
    Reduces a point's coordinates according to a folding instruction, effectively
    reflecting the point across a line defined by the instruction's axis and value.

    Args:
        instruction (Tuple[str, int]): Represented as a string and an integer,
            where the string specifies the axis to fold along ('x' or 'y') and the
            integer specifies the fold line.
        coordinates (Tuple[int, int]): Represented as a pair of integers, where
            the first integer represents the x-coordinate and the second integer
            represents the y-coordinate of a point in a 2D space.

    Returns:
        Tuple[int,int]: The coordinates of the point after applying the given fold
        instruction.

    """
    if instruction[0] == 'x' and coordinates[0] > instruction[1]:
        coordinates = (2 * instruction[1] - coordinates[0], coordinates[1])
    if instruction[0] == 'y' and coordinates[1] > instruction[1]:
        coordinates = (coordinates[0], 2 * instruction[1] - coordinates[1])
    return coordinates


def fold_set(instructions, coordinates_set):
    """
    Applies a sequence of folding instructions to a given set of coordinates. It
    uses a set comprehension to update the coordinates set after each fold,
    effectively applying the transformation defined by the `fold_point` function.

    Args:
        instructions (List[Tuple[str, str]]): Interpreted as a sequence of folding
            instructions. Each instruction is a pair of strings, typically in the
            format ('x', 'n') or ('y', 'n'), where 'n' is the fold position.
        coordinates_set (Set[Point]): Represented as a set of points, where each
            point is a pair of x and y coordinates.

    Returns:
        Set[Point]: A set of points after applying all the folding instructions
        to the original set of coordinates.

    """
    for instruction in instructions:
        coordinates_set = {fold_point(instruction, p) for p in coordinates_set}
    return coordinates_set

if __name__ == '__main__':
    input = open('13/input').read().strip().split('\n\n')
    coordinates = set([tuple([int(y) for y in x.split(',')]) for x in input[0].split('\n')])
    folds = [(x[11], int(x[13:])) for x in input[1].split('\n')]
    print(coordinates, folds)
    print("Part 1:", len(fold_set([folds[0]], coordinates)))
    
    folded_coordinates = fold_set(folds, coordinates)
    text_array = np.zeros((
        max([x[1] + 1 for x in folded_coordinates]),
        max([x[0] + 1 for x in folded_coordinates])
        ), dtype = int)
    for c in folded_coordinates:
        text_array[c[1], c[0]] = 1
    np.savetxt('13/output', text_array, fmt='%d')
    


