import numpy as np
from dataclasses import dataclass

@dataclass
class Cuboid:
    xmin: int
    xmax: int
    ymin: int
    ymax: int
    zmin: int
    zmax: int
    xrange: ()
    command: bool

    def __post_init__(self):
        self.xrange = (xmin, xmax)
        self.yrange = (ymin, ymax)
        self.zrange = (zmin, zmax)

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


command, cuboid, cuboid_array = parse_line("on x=-20..26,y=-36..17,z=-47..7")
cuboid = parse_line_2("on x=-20..26,y=-36..17,z=-47..7")

print(cuboid)

#print(cuboid)
#print(cuboid_array[25:35, 10:20, 0:10])

def update_cuboids(cuboids, new_cuboid):
    updated_cuboids = []
    for cuboid in cuboids:
        union_cuboids = get_union(cuboid, new_cuboid)
        updated_cuboids += union_cuboids
    return updated_cuboids

def get_union(cuboid1, cuboid2):
    if (
        cuboid1.xmax < cuboid2.xmin or
        cuboid1.xmin > cuboid2.xmax or
        cuboid1.ymax < cuboid2.ymin or
        cuboid1.ymin > cuboid2.ymax or
        cuboid1.zmax < cuboid2.zmin or
        cuboid1.zmin > cuboid2.zmax or
    ):
        sub_cuboid1 = [cuboid1]
    else:
        intersection_type = get_intersection_type(quboid1, quboid2)
        
        
        
    if cuboid2.command:
        return sub_cuboid1 + [cuboid2]
    else:
        return sub_cuboid1


if __name__ == "__main__":
    input = open('22/mini_input').readlines()
    engine_array = np.zeros((101, 101, 101))
    cuboids = [parse_line_2(line) for line in input]
    print(min([c[1][0][0] for c in cuboids]))
    print(min([c[1][1][0] for c in cuboids]))
    print(min([c[1][2][0] for c in cuboids]))
    print(max([c[1][0][1] for c in cuboids]))
    print(max([c[1][1][1] for c in cuboids]))
    print(max([c[1][2][1] for c in cuboids]))

    for c in cuboids:
        if c[0] == "on":
            engine_array = ((engine_array + c[2]) >= 1).astype(int)
        if c[0] == "off":
            engine_array = ((engine_array - c[2]) > 0).astype(int)
    print("Part 1:", np.sum(engine_array, axis=(0,1,2)))
