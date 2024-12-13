import numpy as np
from dataclasses import dataclass
from collections import defaultdict
from copy import deepcopy

@dataclass
class Cuboid:
    """
    Represents a 3D cuboid with defined boundaries in the x, y, and z axes. It
    includes a `command` flag and calculates the cuboid's volume in the `__post_init__`
    method.

    Attributes:
        xmin (int): Representing the minimum x-coordinate of a cuboid's boundaries.
        xmax (int): Defined as the maximum value of the x-coordinate of the cuboid.
        ymin (int): Defined as the minimum y-coordinate of the cuboid.
        ymax (int): Defined as the maximum y-coordinate of the cuboid.
        zmin (int): Represented by the lower bound of the z-axis of the cuboid.
        zmax (int): Represented by the maximum z-coordinate of the cuboid, indicating
            the upper boundary of the cuboid in the z-axis.
        command (bool): Initialized to a boolean value, which indicates whether a
            command is associated with the cuboid.

    """
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
    """
    Takes a string line as input, extracts a command and a cuboid description,
    interprets the cuboid description as a 3D coordinates range, and creates a 3D
    NumPy array to represent the cuboid, marking it as filled.

    Args:
        line (str): Expected to be a string representing a line from the input
            data, where each line is expected to be in the format "on/off x,y,z,w,v,u".

    Returns:
        tuple[str,list[int],numpyndarray]: A tuple containing a command string, a
        list of cuboid coordinates, and a 3D NumPy array representing the cuboid.

    """
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
    """
    Parses a line of input to create a Cuboid object. It splits the line into a
    command and coordinates, then extracts the x, y, and z bounds from the
    coordinates. It uses this information to initialize a Cuboid object with the
    given parameters.

    Args:
        line (str): Expected to be a string representing multiple coordinates
            separated by commas with ranges of integers separated by '..' and
            possibly preceded by a command.

    Returns:
        Cuboid: An object with seven attributes: `command`, `xmin`, `xmax`, `ymin`,
        `ymax`, `zmin`, and `zmax`, representing the command and the coordinates
        of a cuboid in three-dimensional space.

    """
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
    """
    Calculates the intersection of two cuboids in 3D space. It returns the
    intersecting cuboid if the input cuboids overlap, otherwise it returns None.
    The intersection is computed by finding the maximum of the minimum coordinates
    and the minimum of the maximum coordinates for each dimension.

    Args:
        cuboid1 (Cuboid): Expected to contain information about a three-dimensional
            cuboid, such as its minimum and maximum x, y, and z coordinates.
        cuboid2 (Cuboid): Used to represent a three-dimensional cuboid, containing
            attributes such as xmin, xmax, ymin, ymax, zmin, and zmax, which
            describe its position and size in a 3D space.

    Returns:
        Cuboid: Defined as a new cuboid object with attributes representing the
        intersection of the input cuboids.

    """
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
    """
    Calculates the increase in size of a set of cuboids after the addition of a
    new cuboid, considering any overlap. It returns the size increase and the
    updated union of all cuboids.

    Args:
        cuboids_dict (Dict[Cuboid, Cuboid]): Presumably a dictionary where the
            keys and values are both instances of the `Cuboid` class, likely
            representing cuboids in a 3D space.
        next_cuboid (Cuboid): Expected to have a `command` attribute and a `volume`
            attribute.

    Returns:
        tuple[int,Dict[str,Cuboid]]: A tuple containing two values:
        
        1/ An integer representing the increase in size of the cuboids.
        2/ A dictionary of cuboids representing the union of the current cuboids
        and the new cuboid.

    """
    size_increase = 0
    if next_cuboid.command:
        size_increase = next_cuboid.volume - size_intersection(cuboids_dict, next_cuboid)
    return size_increase, get_cuboid_union(cuboids_dict, next_cuboid)

def get_cuboid_union(cuboids_dict: defaultdict, next_cuboid):
    """
    Updates a dictionary of cuboids by adding a new cuboid and merging it with
    existing cuboids through their intersections, resulting in a new dictionary
    with updated cuboid sets at each dimension.

    Args:
        cuboids_dict (defaultdict): Expected to be a dictionary where each key
            represents a dimension and each value is a list of cuboids in that dimension.
        next_cuboid (Dict[str, int]): Represented as a cuboid, which is a dictionary
            with integer values, where each key is a dimension and each value is
            an integer.

    Returns:
        Dict[int,List[Cuboid]]: A dictionary where each key is a dimension and
        each value is a list of cuboids that are present at that dimension after
        combining the given cuboid with the existing cuboids.

    """
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
    """
    Calculates the net change in volume when adding a new cuboid to a collection
    of cuboids. It iterates over each cuboid in the collection, checks for
    intersection with the new cuboid, and adjusts the net volume accordingly based
    on the dimension and intersection volume.

    Args:
        cuboids_dict (Dict[str, List[Cuboid]]): Representing a dictionary where
            keys are dimensions (strings) and values are lists of cuboids (objects)
            in those dimensions.
        next_cuboid (Dict[str, Cuboid]): Represented as a dictionary where keys
            are dimensions and values are cuboids, likely representing the next
            cuboid in a series of cuboids.

    Returns:
        int: The total change in volume of the cuboids in `cuboids_dict` due to
        the intersection with `next_cuboid`, considering positive and negative
        intersections based on the dimension `d`.

    """
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
