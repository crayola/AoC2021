def grow_path_1(path):
    """
    Generates all possible paths from a given path in a graph, where the path ends
    at a node labeled 'end'. It recursively explores all possible next nodes,
    allowing uppercase nodes to be visited multiple times but lowercase nodes only
    once.

    Args:
        path (List[str]): Representing a list of locations in a path that is being
            explored in a graph.

    Returns:
        List[List[str]]: A list of all possible paths from the given start path
        to the end point 'end' in the graph defined by the edges list.

    """
    paths = []
    visited = set(path)
    if path[-1] == 'end':
        paths.append(path)
    possible_next = [x[1] for x in edges if 
    (x[0] == path[-1]) and 
        (x[1].isupper() or 
            (x[1].islower() and (x[1] not in visited)))]
    for e in possible_next:
        paths += grow_path_1(path + [e])
    return paths

def grow_path_2(path, visit_dict):
    """
    Generates all possible paths in a graph that end at a specified node ('end')
    without revisiting any node more than twice, adhering to specific rules for
    uppercase and lowercase node connections.

    Args:
        path (List[str]): Constructed recursively by appending adjacent nodes to
            a path starting from the 'start' node. It represents a list of adjacent
            nodes in a graph, where each node is a string.
        visit_dict (Dict[str, int]): Used to keep track of each lowercase cave's
            visit count during the path generation process. It maps each cave to
            its visit count.

    Returns:
        List[List[str]]: A list of all possible paths from the start node 'start'
        to the end node 'end' in the given graph, considering the rules for visiting
        small caves.

    """
    paths = []
    visited_twice = max(visit_dict.values()) == 2
    if path[-1] == 'end':
        paths.append(path)
        return paths
    possible_next = [
        x[1] for x in edges if 
        ((x[1] != 'start') and (x[0] == path[-1]) and 
            (x[1].isupper() or 
                (x[1].islower() and (not visited_twice) and (visit_dict[x[1]] == 1)) or
                (x[1].islower() and (visit_dict[x[1]] == 0))))
            ]
    for e in possible_next:
        if e.isupper():
            paths += grow_path_2(path + [e], visit_dict)
        if e.islower():
            paths += grow_path_2(path + [e], {**visit_dict, e: visit_dict[e]+1})
    return paths

if __name__ == "__main__":
    edges = [tuple(x.strip().split('-')) for x in open('12/input').readlines()]
    edges = edges + [(x[1], x[0]) for x in edges]
    vertices = set({x[0] for x in edges}).union({x[1] for x in edges})
    print("Part 1:", len(grow_path_1(['start'])))
    print("Part 2:", len(grow_path_2(['start'], {x: 0 for x in vertices if x.islower()})))
