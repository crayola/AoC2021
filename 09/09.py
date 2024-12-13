import numpy as np

def parse_input(file):
    """
    Reads input from a specified file, converts each line into a list of integers,
    and then combines these lists into a 2D NumPy array, where each element
    represents the height at a given location.

    Args:
        file (str): Expected to be the path to a file containing input data in a
            format suitable for parsing.

    Returns:
        npndarray[int]: A two-dimensional array of integers representing the input
        file's content, where each inner list has been converted to a row in the
        array.

    """
    lines = open(file).readlines()
    lines = [[int(x) for x in l.strip()] for l in lines]
    heights_array = np.array(lines, dtype=int)
    return heights_array

def shift_array(array, direction):
    """
    Shifts the input array in a specified direction, inserting infinity values at
    the edges of the shifted area. The function supports horizontal and vertical
    shifts to the left, right, up, and down, and returns the resulting shifted array.

    Args:
        array (np.ndarray): Represented by the variable `heights_array`, indicating
            that it is an array of height values.
        direction (Tuple[int, int]): Used to specify the direction and axis of the
            array shift.

    Returns:
        npndarray: An array with the same shape as `heights_array`, but with rows
        or columns shifted by a specified direction, and the edges replaced with
        infinite values.

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
    Identifies low points in a 2D array of heights by comparing each element to
    its neighbors. A low point is defined as a cell that is lower than all its
    adjacent cells.

    Args:
        heights_array (numpy.ndarray): Represented as a two-dimensional array,
            where each element at a given index represents the height of a location
            in a grid or map.

    Returns:
        ndarray[bool]: A boolean mask indicating the presence of a low point at
        each location in the input array.

    """
    shift_up = shift_array(heights_array, (-1, 0))
    shift_down = shift_array(heights_array, (1, 0))
    shift_left = shift_array(heights_array, (0, -1))
    shift_right = shift_array(heights_array, (0, 1))
    low_points = heights_array < np.minimum.reduce([shift_down, shift_left, shift_right, shift_up])
    return low_points

def grow_basin(heights_array, low_point):
    """
    Identifies and expands a low-point basin in a 2D grid of heights, where a basin
    is a set of connected points with heights less than 9. It recursively adds
    neighboring points with heights less than 9 to the basin until no more points
    can be added.

    Args:
        heights_array (numpy.ndarray): Expected to represent a 2D grid of integers
            where each integer represents the height of a point in the grid.
        low_point (Tuple[int, int]): Representing the coordinates of a low point
            in the `heights_array`.

    Returns:
        Set[tuple[int,int]]: The coordinates of all points in a basin, where a
        basin is defined as a group of points with a height of less than 9 surrounding
        a low point.

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
