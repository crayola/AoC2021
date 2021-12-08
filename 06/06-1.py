def parse_input(file):
    parsed_str = open(file, 'r').read().split(',')
    list_fish = [int(x) for x in parsed_str]
    dict_fish = {n_fish: len([x for x in list_fish if x == n_fish]) for n_fish in range(9)}
    return dict_fish

def iterate_fish(fish_dict):
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
