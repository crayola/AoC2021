import numpy as np

def octoplosions(octopi):
    octo_locations = np.argwhere(octopi>=10)
    for o in octo_locations:
        for i in range(max(0, o[0]-1), min(octopi.shape[0], o[0]+2)):
            for j in range(max(0, o[1]-1), min(octopi.shape[1], o[1]+2)):
                octopi[i, j] += 1
        octopi[o[0], o[1]] = - 9 # to remember it flashed
    return octopi

def increment_octopi(octopi):
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