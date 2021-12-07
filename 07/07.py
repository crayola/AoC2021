import numpy as np

def parse_input(file):
    crabs = np.loadtxt(file, delimiter=',')
    return crabs

def part_2_total_spend(crabs, target):
    dist = np.absolute(crabs - target)
    return np.sum(dist * (dist + 1) / 2)

def brute_force(crabs):
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

