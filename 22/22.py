import numpy as np
from dataclasses import dataclass
from collections import defaultdict
from copy import deepcopy

@dataclass
class Cuboid:
    xmin: int
    xmax: int
    ymin: int
    ymax: int
    zmin: int
    zmax: int
    command: bool

    def __post_init__(self):
        self.volume = (self.xmax - self.xmin + 1) * (self.ymax - self.ymin + 1) * (self.zmax - self.zmin + 1)

def parse_line(line):
    command, line = line.split(' ')
    cuboid = line.split(',')
    cuboid = [[int(x) + 50 for x in coord[2:].split('..')] for coord in cuboid]
    cuboid_array = np.zeros((101, 101, 101))
    cuboid_array[
        cuboid[0][0]:cuboid[0][1] + 1, 
        cuboid[1][0]:cuboid[1][1] + 1, 
        cuboid[2][0]:cuboid[2][1] + 1, 
        ] = 1
    return command, cuboid, cuboid_array

def parse_line_2(line):
    command, line = line.split(' ')
    line = [[int(x) for x in coord[2:].split('..')] for coord in line.split(',')]
    cuboid = Cuboid(
        command = command == "on",
        xmin = line[0][0],
        xmax = line[0][1],
        ymin = line[1][0],
        ymax = line[1][1],
        zmin = line[2][0],
        zmax = line[2][1],
    )
    return cuboid

def get_intersection(cuboid1, cuboid2) -> Cuboid:
    if (
        cuboid1.xmax < cuboid2.xmin or
        cuboid1.xmin > cuboid2.xmax or
        cuboid1.ymax < cuboid2.ymin or
        cuboid1.ymin > cuboid2.ymax or
        cuboid1.zmax < cuboid2.zmin or
        cuboid1.zmin > cuboid2.zmax):
        return None
    else:
        return Cuboid(
            command = 1,
            xmin = max(cuboid1.xmin, cuboid2.xmin),
            xmax = min(cuboid1.xmax, cuboid2.xmax),
            ymin = max(cuboid1.ymin, cuboid2.ymin),
            ymax = min(cuboid1.ymax, cuboid2.ymax),
            zmin = max(cuboid1.zmin, cuboid2.zmin),
            zmax = min(cuboid1.zmax, cuboid2.zmax),
            )

def update_cuboids(cuboids_dict, next_cuboid: Cuboid):
    size_increase = 0
    if next_cuboid.command:
        size_increase = next_cuboid.volume - size_intersection(cuboids_dict, next_cuboid)
    return size_increase, get_cuboid_union(cuboids_dict, next_cuboid)

def get_cuboid_union(cuboids_dict: defaultdict, next_cuboid):
    new_cuboids_dict = deepcopy(cuboids_dict)
    new_cuboids_dict[0] += [next_cuboid]
    for d, v in cuboids_dict.items():
        for cuboid in v:
            intersection = get_intersection(cuboid, next_cuboid)
            #print(cuboid, next_cuboid, intersection)
            if intersection:
                new_cuboids_dict[d + 1].append(intersection)
    return new_cuboids_dict

def size_intersection(cuboids_dict, next_cuboid):
    size = 0
    for d, v in cuboids_dict.items():
        for cuboid in v:
            intersection = get_intersection(cuboid, next_cuboid)
            if intersection:
                size += (-1 if (d % 2) else +1) * intersection.volume
    return size
    


if __name__ == "__main__":
    input = open('22/input').readlines()

    # Part 1:
    engine_array = np.zeros((101, 101, 101))
    cuboids = [parse_line(line) for line in input]
    for c in cuboids:
        if c[0] == "on":
            engine_array = ((engine_array + c[2]) >= 1).astype(int)
        if c[0] == "off":
            engine_array = ((engine_array - c[2]) > 0).astype(int)
    print("Part 1:", np.sum(engine_array, axis=(0,1,2)))

    # Part 2:
    cuboids = [parse_line_2(line) for line in input]
    cuboids_dict = defaultdict(list)
    size = 0
    steps = 0
    for c in cuboids[::-1]:
        size_increase, cuboids_dict = update_cuboids(cuboids_dict, c)
        size += size_increase
        steps += 1
        if steps > 250 and steps % 10 == 0:
            print("Steps completed:", steps, "\tSteps left:", len(cuboids) - steps)
    print("Part 2:", size)
