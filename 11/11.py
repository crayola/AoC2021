import numpy as np

def octoplosions(octopi):
    """
    Simulates an explosion of an octopus in a grid. It identifies locations with
    energy levels greater than or equal to 10, increments neighboring cells by 1,
    and then sets the original cell to -9, indicating a new octopus has formed.

    Args:
        octopi (Any): Assumed to be a 2D NumPy array where each element represents
            the energy level of an octopus.

    Returns:
        ndarray: An array of integers representing the state of the octopuses after
        the explosion.

    """
    octo_locations = np.argwhere(octopi>=10)
    for o in octo_locations:
        for i in range(max(0, o[0]-1), min(octopi.shape[0], o[0]+2)):
            for j in range(max(0, o[1]-1), min(octopi.shape[1], o[1]+2)):
                octopi[i, j] += 1
        octopi[o[0], o[1]] = - 9 # to remember it flashed
    return octopi

def increment_octopi(octopi):
    """
    Simulates the process of incrementing the energy levels of a grid of octopuses,
    detecting and resolving any flashes that occur as a result, and counting the
    total number of flashes.

    Args:
        octopi (np.ndarray): Representing a 2D array of octopus energy levels,
            where each element in the array corresponds to the energy level of a
            specific octopus.

    Returns:
        Tuple[ndarray,int]: A tuple containing an updated 2D array of octopus
        energy levels and the total number of flashes that occurred during the
        update process.

    """
    octopi += 1
    flashes = 0
    while (octopi >= 10).any():
        flashes += np.sum(octopi >= 10, axis=(0,1))
        octopi = octoplosions(octopi)
    octopi[octopi<0] = 0
    return octopi, flashes

if __name__ == "__main__":
    octopi_input = np.genfromtxt("11/input", delimiter=1, dtype=int)

    # part 1
    octopi = octopi_input.copy()
    count_flashes = 0
    for _ in range(100):
        octopi, flashes = increment_octopi(octopi)
        count_flashes += flashes
    print("Part 1:", count_flashes)

    #part 2
    i = 0
    octopi = octopi_input.copy()
    while (octopi > 0).any():
        octopi, _ = increment_octopi(octopi)
        i += 1
    print("Part 2:", i)