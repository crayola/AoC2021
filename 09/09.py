import numpy as np

def parse_input(file):
    lines = open(file).readlines()
    lines = [[int(x) for x in l.strip()] for l in lines]
    heights_array = np.array(lines)
    return(heights_array)

def shift_array(array, direction):
    if direction == (-1, 0):
        shifted_array = np.hstack((heights_array[:, 1:], np.ones((hdim, 1)) * np.inf))
    elif direction == (1, 0):
        shifted_array = np.hstack((np.ones((hdim, 1)) * np.inf, heights_array[:, :-1]))
    elif direction == (0, 1):
        shifted_array = np.vstack((np.ones((1, vdim)) * np.inf, heights_array[:-1,:]))
    elif direction == (0, -1):
        shifted_array = np.vstack((heights_array[1:,:], np.ones((1, vdim)) * np.inf))
    return(shifted_array)

def find_low_points(heights_array):
    vdim = heights_array.shape[0]
    hdim = heights_array.shape[1]
    shift_up = shift_array(heights_array, (-1, 0))
    shift_down = shift_array(heights_array, (1, 0))
    shift_left = shift_array(heights_array, (0, -1))
    shift_right = shift_array(heights_array, (0, 1))
    low_points = heights_array < np.minimum.reduce([shift_down, shift_left, shift_right, shift_up])
    return(low_points)

def grow_basin(heights_array, low_point):
    basin = set(np.argwhere(low_point==1))
    new_basin = {}
    while new_basin != basin:
        basin_candidates = basin
        basin_candidates.union({x + np.array([1,0]) for x in basin_candidates})
        basin_candidates.union({x + np.array([-1,0]) for x in basin_candidates})
        basin_candidates.union({x + np.array([0,1]) for x in basin_candidates})
        basin_candidates.union({x + np.array([0,-1]) for x in basin_candidates})
        for x in 
        basin_candidates = ((shift_up + shift_down + shift_left + shift_right) >= 1 - basin)



if __name__ == "__main__":
    heights_array = parse_input("09/input")
    print(np.sum((heights_array + 1) * find_low_points(heights_array), axis = (0,1)))
