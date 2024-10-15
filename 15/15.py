import numpy as np

def update_costs(visited: np.ndarray, costs: np.ndarray, risks: np.ndarray):
    """Update costs around current position"""
    current = np.unravel_index(np.argmin(costs + visited), costs.shape)
    visited[current] = np.inf
    for i in range(max(0, current[0]-1), min(costs.shape[0], current[0]+2)):
        for j in range(max(0, current[1]-1), min(costs.shape[1], current[1]+2)):
            if (i == current[0]) != (j == current[1]): # xor
                costs[i, j] = min(costs[i, j], costs[current] + risks[i, j])
    return (visited, costs, risks)

def build_complete_risk_array(r):
    """Provides the input for part 2"""
    vstack = np.vstack([
        r, (r % 9) + 1, ((r + 1) % 9) + 1,
        ((r + 2) % 9) + 1, ((r + 3) % 9) + 1
        ])
    full_risks = np.hstack([
        vstack, (vstack % 9) + 1, ((vstack + 1) % 9) + 1,
        ((vstack + 2) % 9) + 1, ((vstack + 3) % 9) + 1
        ])
    return full_risks

def find_shortest_path(risks: np.ndarray):
    """
    Determines the minimum cost of traversing a grid with associated risks. It
    uses a Dijkstra's algorithm implementation, updating costs and visited flags
    in each iteration until the shortest path to the last cell is found.

    Args:
        risks (np.ndarray*): Representing a 2D grid of values, likely representing
            risk levels, costs, or weights that need to be considered when finding
            the shortest path.

    Returns:
        float: The minimum cost to reach the bottom-right cell of a grid represented
        by the input `risks` array.

    """
    costs = np.full_like(risks, np.inf, dtype=float)
    visited = np.zeros_like(risks, dtype=float)
    costs[0,0] = 0
    while not visited[-1, -1]:
        visited, costs, _ = update_costs(visited, costs, risks)
    return costs[-1, -1]

if __name__ == "__main__":
    risks_1 = np.genfromtxt("15/input", delimiter=1, dtype=int)
    print("Part 1:", find_shortest_path(risks_1))
    risks_2 = build_complete_risk_array(risks_1)
    print("Part 2:", find_shortest_path(risks_2))