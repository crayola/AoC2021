import numpy as np

def parse_input(file):
    crabs = np.array(open(file).read().strip().split(','), dtype=int)
    return crabs

def part_2_spend(crab, target):
    n_steps = np.absolute(target - crab)
    spent = 0
    for i in range(1, n_steps + 1):
        spent += i
    return spent

def part_2_total_spend(crabs, target):
    return(sum([part_2_spend(crab, target) for crab in crabs]))

def brute_force(crabs):
    for target in range(500):
        print(target, part_2_total_spend(crabs, target))
    return(None)

if __name__ == "__main__":
    crabs = parse_input("07/input")
    print(np.sum(np.absolute(crabs - np.median(crabs)))) #part 1
    print(np.sum(np.absolute(crabs - 458))) #part 2