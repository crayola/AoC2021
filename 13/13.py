import numpy as np

def fold_point(instruction, coordinates):
    """
    Reflects a point across a given fold line in a 2D coordinate system. It takes
    a fold instruction (e.g., 'x=5' or 'y=3') and a point's coordinates as input,
    and returns the coordinates of the reflected point.

    Args:
        instruction (Tuple[str, int]): Used to specify the axis and the fold
            position. It is a tuple containing a string ('x' or 'y') indicating
            the axis to fold along, and an integer representing the fold position.
        coordinates (Tuple[int, int]): Represented as a pair of integers, where
            the first integer is the x-coordinate and the second integer is the
            y-coordinate of a point on a 2D plane.

    Returns:
        Tuple[int,int]: The coordinates of a point after applying a fold instruction
        to it.

    """
    if instruction[0] == 'x' and coordinates[0] > instruction[1]:
        coordinates = (2 * instruction[1] - coordinates[0], coordinates[1])
    if instruction[0] == 'y' and coordinates[1] > instruction[1]:
        coordinates = (coordinates[0], 2 * instruction[1] - coordinates[1])
    return coordinates


def fold_set(instructions, coordinates_set):
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
    


