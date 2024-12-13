def parse_input(file):
    """
    Reads a file, splits its contents into a list of integers, counts the occurrences
    of each integer, and stores these counts in a dictionary. The dictionary keys
    represent the fish ages, and the values represent the number of fish at each
    age.

    Args:
        file (str): Expected to represent a file path. It is used to open a file
            in read mode, allowing the function to read and process its contents.

    Returns:
        Dict[int,int]: A dictionary containing the count of each fish age from 0
        to 8.

    """
    parsed_str = open(file, 'r').read().split(',')
    list_fish = [int(x) for x in parsed_str]
    dict_fish = {n_fish: len([x for x in list_fish if x == n_fish]) for n_fish in range(9)}
    return dict_fish

def iterate_fish(fish_dict):
    """
    Updates a dictionary representing a school of fish, simulating a generation
    of fish by shifting ages and incrementing the count of fish that are 6 days old.

    Args:
        fish_dict (Dict[int, int]): Represented as a dictionary where keys are
            integers from 0 to 8 and values are integers representing the count
            of fish at each stage of their life cycle.

    Returns:
        Dict[int,int]: A dictionary representing the state of fish after one
        generation, where keys are the ages of fish and values are the number of
        fish at each age.

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
