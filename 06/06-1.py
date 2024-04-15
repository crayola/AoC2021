def parse_input(file):
    """
    reads a comma-separated file, splits it into an list of integers, creates a
    dictionary of length counts for each fish species, and returns the dictionary.

    Args:
        file (str): file containing the comma-separated numbers to be parsed and
            converted into a dictionary of length values for each fish species.

    Returns:
        dict: a dictionary containing the length of each fish in the input list.

    """
    parsed_str = open(file, 'r').read().split(',')
    list_fish = [int(x) for x in parsed_str]
    dict_fish = {n_fish: len([x for x in list_fish if x == n_fish]) for n_fish in range(9)}
    return dict_fish

def iterate_fish(fish_dict):
    """
    iterates through a dictionary of fish, updates its values based on the index,
    and returns an updated dictionary with additional calculations for the eighth
    and sixth indexes.

    Args:
        fish_dict (dict): 8-element dictionary of fish, where each element corresponds
            to a different generation in the iterative process.

    Returns:
        dict: a new dictionary containing the next generation of fish, along with
        the total length of the fish in the generation.

    """
    fish_nextgen = {}
    for i in range(8):
        fish_nextgen[i] = fish_dict[i+1]
    fish_nextgen[8] = fish_dict[0]
    fish_nextgen[6] = fish_nextgen[6] + fish_dict[0]
    return fish_nextgen

if __name__ == "__main__":
    fish = parse_input("06/input")
    for i in range(256):
        fish = iterate_fish(fish)
    print(fish)
    print(sum(fish.values()))
