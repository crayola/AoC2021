import numpy as np

def octoplosions(octopi):
    """
    Simulates a local energy release in an octopus grid, incrementing neighboring
    energy levels by 1 and resetting the center energy level to -9.

    Args:
        octopi (np.ndarray): Defined as a 2D array of integers representing locations
            of octopuses in an underwater environment, where higher values indicate
            the energy levels of the octopuses.

    Returns:
        npndarray: Modified octopod energy levels, where each octopus with energy
        level 10 or above has been reduced to -9 and its neighboring octopods have
        had their energy levels increased by 1.

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
    Increments the energy levels of a grid of octopuses by 1, simulates flashes
    based on energy levels, and returns the updated grid and the total number of
    flashes.

    Args:
        octopi (numpy.ndarray): Represented as a two-dimensional array, where each
            element represents the energy level of an octopus in a grid, with
            higher values indicating increased energy.

    Returns:
        Tuple[int,int]: A numpy array representing the state of the octopi grid
        and an integer representing the total number of flashes that occurred
        during the simulation.

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