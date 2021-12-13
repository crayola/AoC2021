from cgitb import text
import numpy as np

def fold_point(instruction, coordinates):
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
    


