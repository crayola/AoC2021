def grow_path_1(path):
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
