import numpy as np

def grow_costs(visited: set, current: tuple, costs: np.ndarray):
    for i in range(max(0, current[0]-1), min(costs.shape[0], current[0]+2)):
        for j in range(max(0, current[1]-1), min(costs.shape[1], current[1]+2)):
            costs[i, j] = min(cost[i, j], costs[current] + risks[i,j])
    visited += current
    if ((costs.shape[0]-1, costs.shape[1]-1) in visited):
        return costs[-1,-1]
    else:
        current = np.logical_not(visited) *
        grow_costs()
        

if __name__ == "__main__":
    risks = np.genfromtxt("15/mini_input", delimiter=1, dtype=int)
    visited = (False * risks).astype(bool)
    costs = np.inf * risks
    costs[0,0] = 0
    print(risks, visited)