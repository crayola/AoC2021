def parse_input(file):
    """
    Reads a file, splits its contents into a list of integers separated by commas,
    counts the occurrences of each integer, and returns a dictionary where the
    keys are the fish ages and the values are their respective counts.

    Args:
        file (str): Expected to be a file path to a file containing comma-separated
            numbers representing fish ages.

    Returns:
        Dict[int,int]: A dictionary where the keys are the fish ages (integers
        from 0 to 8) and the values are the counts of fish at each age.

    """
    parsed_str = open(file, 'r').read().split(',')
    list_fish = [int(x) for x in parsed_str]
    dict_fish = {n_fish: len([x for x in list_fish if x == n_fish]) for n_fish in range(9)}
    return dict_fish

def iterate_fish(fish_dict):
    """
    Updates a dictionary representing a generation of fish, simulating the passage
    of time. It shifts each fish's generation by one day and updates the population
    of fish that give birth to new fish on the sixth day.

    Args:
        fish_dict (Dict[int, int]): Representing the initial state of a school of
            fish, where the keys are the days since a fish was spawned and the
            values are the number of fish at each stage.

    Returns:
        Dict[int,int]: A dictionary representing the state of a school of fish
        after one generation, where keys are the fish ages and values are the
        number of fish at each age.

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
