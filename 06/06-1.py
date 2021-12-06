def parse_input(file):
    parsed_str = open(file, 'r').read().split(',')
    return [int(x) for x in parsed_str]

def count_fish(fish_raw):
    dictfish = {}
    dictfish["0"] = len([x for x in fish_raw if x == 0])
    dictfish["1"] = len([x for x in fish_raw if x == 1])
    dictfish["2"] = len([x for x in fish_raw if x == 2])
    dictfish["3"] = len([x for x in fish_raw if x == 3])
    dictfish["4"] = len([x for x in fish_raw if x == 4])
    dictfish["5"] = len([x for x in fish_raw if x == 5])
    dictfish["6"] = len([x for x in fish_raw if x == 6])
    dictfish["7"] = len([x for x in fish_raw if x == 7])
    dictfish["8"] = len([x for x in fish_raw if x == 8])
    return(dictfish)

def iterate_one_fish(fish):
    if fish == 0:
        return [6, 0]
    if fish > 0:
        return [fish - 1]


def iterate_fish(fish_dict):
    dict_return = {}
    dict_return["8"] = fish_dict["0"]
    dict_return["6"] = fish_dict["0"] + fish_dict["7"]
    dict_return["7"] = fish_dict["8"]
    dict_return["5"] = fish_dict["6"]
    dict_return["4"] = fish_dict["5"]
    dict_return["3"] = fish_dict["4"]
    dict_return["2"] = fish_dict["3"]
    dict_return["1"] = fish_dict["2"]
    dict_return["0"] = fish_dict["1"]
    return dict_return


if __name__ == "__main__":
    fish_ini = parse_input("06/input")
    fish_counts = count_fish(fish_ini)
    print(fish_counts)
    fish = fish_counts
    for i in range(256):
        fish = iterate_fish(fish)
        print(i)
    print(fish)
    print(
        fish["0"] + fish["1"] +
        fish["2"] + fish["3"] +
        fish["4"] + fish["5"] +
        fish["6"] + fish["7"] + fish["8"]
    )
