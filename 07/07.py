import numpy as np

def parse_input(file):
    """
    Loads data from a specified file into a numpy array, where each row represents
    a single data point, and returns the array of data points.

    Args:
        file (str): A path to a file containing comma-separated values (CSV)
            representing the positions of crabs.

    Returns:
        npndarray: A 1D array of floats representing the positions of crabs.

    """
    crabs = np.loadtxt(file, delimiter=',')
    return crabs

def part_2_total_spend(crabs, target):
    """
    Calculates the total fuel cost for a list of crabs to move to a specified
    target position. It uses the formula for the sum of the first `n` positive
    integers, where `n` is the distance each crab must move.

    Args:
        crabs (List[int]): Expected to contain a list of integers representing the
            positions of crabs in a horizontal line.
        target (int): Defined as the optimal horizontal position for the crabs to
            align at, minimizing the total fuel cost.

    Returns:
        int: The total fuel cost for all crabs to move to the target position.

    """
    dist = np.absolute(crabs - target)
    return np.sum(dist * (dist + 1) / 2)

def brute_force(crabs):
    """
    Finds the optimal alignment point for a list of crabs by incrementally increasing
    the target position and calculating the total fuel spent using the
    `part_2_total_spend` function, stopping when fuel spent starts to increase.

    Args:
        crabs (List[int]): Assumed to be a list of integers representing the
            positions of crabs in a horizontal line on a number line, likely
            requiring alignment for fuel efficiency.

    Returns:
        Tuple[int,int]: A pair of values. The first value represents the optimal
        target position to align all crabs, and the second value represents the
        total fuel spent to align all crabs at this optimal position.

    """
    total_spend = np.Inf
    target = 0
    while True:
        total_spend_next = part_2_total_spend(crabs, target)
        if total_spend_next > total_spend:
            break
        total_spend = total_spend_next
        target += 1
    return(target - 1, total_spend)

if __name__ == "__main__":
    crabs = parse_input("07/input")

    # part 1
    print(np.sum(np.absolute(crabs - np.median(crabs))))
    
    # part 2
    print(brute_force(crabs))
    
    # also part 2
    avg_pos = np.mean(crabs)
    print(min([
        part_2_total_spend(crabs, int(avg_pos)),
        part_2_total_spend(crabs, int(avg_pos) - 1),
        part_2_total_spend(crabs, int(avg_pos) + 1)
    ])) # brute-forcing around the approximate minimum :-D

