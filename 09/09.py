import numpy as np

def parse_input(file):
    """
    Reads specified file, strips newline characters, converts each line into a
    list of integers, and converts the list of lists into a 2D numpy array of integers.

    Args:
        file (str): Used to specify the path to a file containing input data.

    Returns:
        npndarray[int]: A two-dimensional array of integers representing the input
        file's height values.

    """
    lines = open(file).readlines()
    lines = [[int(x) for x in l.strip()] for l in lines]
    heights_array = np.array(lines, dtype=int)
    return heights_array

def shift_array(array, direction):
    """
    Shifts the values in a 2D array, effectively inserting a row or column of
    infinite values at the specified direction.

    Args:
        array (numpy.ndarray): Expected to represent a 2D array of height values,
            referred to as `heights_array` within the function.
        direction (Tuple[int, int]): Used to specify the direction of the shift
            operation. It is a 2-element tuple where the first element represents
            the row direction (positive for up, negative for down) and the second
            element represents the column direction (positive for right, negative
            for left).

    Returns:
        numpyndarray: A two-dimensional array with the input array `heights_array`
        shifted in the specified direction. The shift is achieved by appending or
        prepending rows or columns of infinite values.

    """
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
    """
    Identifies low points in a 2D array of heights by comparing each element with
    its neighboring elements. It returns a boolean array where `True` indicates a
    low point, i.e., a point with a height lower than its neighbors.

    Args:
        heights_array (numpy.ndarray): 2D array representing a grid of heights,
            where each element corresponds to a cell's height in the grid.

    Returns:
        npndarray[bool]: A boolean mask indicating the positions of low points in
        the input array.

    """
    shift_up = shift_array(heights_array, (-1, 0))
    shift_down = shift_array(heights_array, (1, 0))
    shift_left = shift_array(heights_array, (0, -1))
    shift_right = shift_array(heights_array, (0, 1))
    low_points = heights_array < np.minimum.reduce([shift_down, shift_left, shift_right, shift_up])
    return low_points

def grow_basin(heights_array, low_point):
    """
    Identifies and expands a low-lying basin in a 2D array of heights, following
    a set of rules to determine neighboring points that are part of the basin.

    Args:
        heights_array (ndarray): Expected to be a two-dimensional array of integers
            representing a landscape of elevation values.
        low_point (Tuple[int, int]): Used to specify the coordinates of a low point
            in the `heights_array`.

    Returns:
        Set[Tuple[int,int]]: A set of coordinates representing the points in a
        basin of a height map.

    """
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
