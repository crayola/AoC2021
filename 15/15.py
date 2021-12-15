import numpy as np

import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(100000)

def grow_costs(step, visited: np.ndarray, current: tuple, costs: np.ndarray, risks: np.ndarray):
    #print(visited, costs, current)
    print(step)
    if current == (costs.shape[0]-1, costs.shape[1]-1):
        return costs[-1,-1]
    for i in range(max(0, current[0]-1), min(costs.shape[0], current[0]+2)):
        for j in range(max(0, current[1]-1), min(costs.shape[1], current[1]+2)):
            if (i == current[0]) != (j == current[1]): # xor
                #print(i,j)
                costs[i, j] = min(costs[i, j], costs[current] + risks[i, j])
    visited[current] = True
    #print(costs, visited)
    #print(costs + distance_from_bottomright + 1000 * visited)
    costs.shape[0] - current[0] + costs.shape[1] - current[1] 
    current = np.unravel_index(np.argmin(costs + 1000 * visited), costs.shape)
    #print(current)
    return grow_costs(step+1, visited, current, costs, risks)

def grow_costs_2(visited: np.ndarray, current: tuple, costs: np.ndarray, risks: np.ndarray):
    #print(visited, costs, current)
    if current == (costs.shape[0]-1, costs.shape[1]-1):
        print(costs[-1,-1])
        return costs[-1,-1]
    for i in range(max(0, current[0]-1), min(costs.shape[0], current[0]+2)):
        for j in range(max(0, current[1]-1), min(costs.shape[1], current[1]+2)):
            if (i == current[0]) != (j == current[1]): # xor
                #print(i,j)
                costs[i, j] = min(costs[i, j], costs[current] + risks[i, j])
    visited[current] = True
    current = np.unravel_index(np.argmin(costs + 10000 * visited), costs.shape)
    return (visited, current, costs, risks)

def complete_risk(risks):
    verticalstack = np.vstack([
        risks, 
        (risks % 9) + 1,
        ((risks + 1) % 9) + 1,
        ((risks + 2) % 9) + 1,
        ((risks + 3) % 9) + 1
    ])
    return np.hstack([
        verticalstack, 
        (verticalstack % 9) + 1,
        ((verticalstack + 1) % 9) + 1,
        ((verticalstack + 2) % 9) + 1,
        ((verticalstack + 3) % 9) + 1
    ])
        


if __name__ == "__main__":
    risks = np.genfromtxt("15/input", delimiter=1, dtype=int)
    visited = (False * risks).astype(bool)
    costs = np.inf * risks
    costs[0,0] = 0
    distance_from_bottomright = costs * 0
    for i in range(costs.shape[0]):
        for j in range(costs.shape[1]):
            distance_from_bottomright[i, j] = costs.shape[0] - i + costs.shape[1] - j
    print(distance_from_bottomright)
    print(risks, visited)
    #print("Part 1:", grow_costs(0, visited, (0,0), costs, risks))
    big_risks = complete_risk(risks)
    big_visited = (False * big_risks).astype(bool)
    big_costs = np.inf * big_risks
    big_costs[0,0] = 0
    current = (0,0)
    i = 0
    while True:
        i += 1
        if i % 10000 == 0: print(i, current, big_costs[-10:,-10:], )
        big_visited, current, big_costs, big_risks = grow_costs_2(big_visited, current, big_costs, big_risks)
    

