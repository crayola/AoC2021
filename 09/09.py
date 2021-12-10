import numpy as np

def parse_input(file):
    lines = open(file).readlines()
    lines = [[int(x) for x in l.strip()] for l in lines]
    heights_array = np.array(lines, dtype=int)
    return heights_array

def shift_array(array, direction):
    nrows = heights_array.shape[0]
    ncols = heights_array.shape[1]
    if direction == (-1, 0): # up
        shifted_array = np.vstack((heights_array[1:, :], np.ones((1, ncols)) * np.inf))
    elif direction == (1, 0): # down
        shifted_array = np.vstack((np.ones((1, ncols)) * np.inf, heights_array[:-1, :]))
    elif direction == (0, 1): # right
        shifted_array = np.hstack((np.ones((nrows, 1)) * np.inf, heights_array[:,:-1]))
    elif direction == (0, -1): #left
        shifted_array = np.hstack((heights_array[:,1:], np.ones((nrows, 1)) * np.inf))
    return shifted_array

def find_low_points(heights_array):
    shift_up = shift_array(heights_array, (-1, 0))
    shift_down = shift_array(heights_array, (1, 0))
    shift_left = shift_array(heights_array, (0, -1))
    shift_right = shift_array(heights_array, (0, 1))
    low_points = heights_array < np.minimum.reduce([shift_down, shift_left, shift_right, shift_up])
    return low_points

def grow_basin(heights_array, low_point):
    nrows = heights_array.shape[0]
    ncols = heights_array.shape[1]
    basin = {}
    new_basin = set([low_point])
    while new_basin != basin:
        basin = new_basin.copy()
        basin_candidates = basin.copy()
        basin_candidates.update({(x[0] + 1, x[1]) for x in basin if x[0] < nrows - 1})
        basin_candidates.update({(x[0] - 1, x[1]) for x in basin if x[0] > 0})
        basin_candidates.update({(x[0], x[1] + 1) for x in basin if x[1] < ncols - 1})
        basin_candidates.update({(x[0], x[1] - 1) for x in basin if x[1] > 0})
        for cand in basin_candidates.difference(basin):
            if heights_array[cand] < 9:
                new_basin.add(cand)
    return new_basin

if __name__ == "__main__":
    heights_array = parse_input("09/input")

    low_points = find_low_points(heights_array)
    print("Part 1:", np.sum((heights_array + 1) * low_points, axis = (0,1)))

    low_points_tuples = [tuple(x) for x in np.argwhere(low_points)]
    basins = [grow_basin(heights_array, x) for x in low_points_tuples]
    basin_sizes = sorted([len(x) for x in basins], reverse=True)
    print("Part 2:", basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
