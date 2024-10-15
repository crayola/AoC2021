import numpy as np
from dataclasses import dataclass
from collections import defaultdict
from copy import deepcopy

@dataclass
class Cuboid:
    """
    Represents a three-dimensional rectangular prism. It stores the coordinates
    of its minimum and maximum points in 3D space and the type of command associated
    with it. The `__post_init__` method calculates the volume of the cuboid.

    Attributes:
        xmin (int*): Defined to represent the minimum x-coordinate of the cuboid.
        xmax (int*): Represented by the maximum x-coordinate of a cuboid in a
            three-dimensional space.
        ymin (int*): Represented by a lower bound of a 3D cuboid's y-coordinate range.
        ymax (int*): Defined as the maximum y-coordinate of the cuboid.
        zmin (int*): Represented as the minimum z-coordinate of the cuboid. It is
            part of the three-dimensional coordinates of the cuboid's boundaries,
            along with `xmin`, `xmax`, `ymin`, `ymax`, and `zmax`.
        zmax (int*): Represented as the maximum z-coordinate of the cuboid. It is
            a required attribute and must be defined when an instance of the
            `Cuboid` class is created.
        command (bool*): Initialized as a boolean value, but its purpose and usage
            are not described in the provided code snippet.

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
    Parses a line of input into a command and a cuboid specification, then creates
    a 3D NumPy array representing the cuboid in a 101x101x101 space.

    Args:
        line (str): Split into two parts: a command and a cuboid specification by
            a space character. The cuboid specification is a string of comma-separated
            coordinates in the format "x..y..z".

    Returns:
        Tuple[str,List[List[int]],ndarray]: A tuple containing three values:
        
        1/  A string representing the command.
        2/  A list of lists of integers representing the cuboid's coordinates.
        3/  A 3D NumPy array representing the cuboid's shape.

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
    Parses a line of input into a Cuboid object. It splits the line into a command
    and coordinates, converts the coordinates into a list of integer pairs, and
    uses these to initialize a Cuboid object with its properties.

    Args:
        line (str): Split into two parts, a command and a set of coordinates, by
            a single space character.

    Returns:
        Cuboid: An object containing the following attributes: command, xmin, xmax,
        ymin, ymax, zmin, and zmax. These attributes represent the state and bounds
        of a 3D cuboid.

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
    Calculates the intersection of two cuboids in 3D space. It checks for overlap
    and returns a new cuboid representing the intersection, or `None` if the cuboids
    do not intersect.

    Args:
        cuboid1 (Cuboid): Expected to have attributes: `xmin`, `xmax`, `ymin`,
            `ymax`, `zmin`, `zmax`, and `command`, representing a cuboid's minimum
            and maximum x, y, z coordinates and a command.
        cuboid2 (Cuboid): Represented by a cuboid in three-dimensional space, which
            has attributes for its minimum and maximum x, y, and z coordinates.

    Returns:
        Cuboid*: A cuboid representing the intersection of two given cuboids. If
        no intersection exists, it returns None.

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
    Calculates the increase in volume of a set of cuboids after adding a new cuboid
    and returns this increase along with the updated union of all cuboids. It
    considers the command of the new cuboid to determine the volume increase.

    Args:
        cuboids_dict (Dict[Cuboid, Cuboid]): Used to store and manage cuboids.
            
            It likely contains existing cuboids as keys and their respective
            properties, such as union or intersection, as values.
        next_cuboid (Cuboid*): Described by its attributes, including a command
            and volume.

    Returns:
        tuple[int,Dict[Cuboid,Cuboid]]: A tuple containing an integer and a
        dictionary. The integer represents the increase in size due to the addition
        of the new cuboid.

    """
    size_increase = 0
    if next_cuboid.command:
        size_increase = next_cuboid.volume - size_intersection(cuboids_dict, next_cuboid)
    return size_increase, get_cuboid_union(cuboids_dict, next_cuboid)

def get_cuboid_union(cuboids_dict: defaultdict, next_cuboid):
    """
    Updates a dictionary of cuboids by adding a new cuboid and merging any
    intersecting cuboids. It uses a recursive approach to find intersections between
    the new cuboid and existing cuboids, adding the intersection to a new dictionary.

    Args:
        cuboids_dict (defaultdict*): Used to store cuboids, where each key represents
            a dimension and its corresponding value is a list of cuboids in that
            dimension.
        next_cuboid (Dict[str, int]): Represented as a cuboid, which is presumably
            a dictionary containing information about a cuboid in 3D space.

    Returns:
        Dict[int,List[Cuboid]]: A dictionary of cuboids, where each key is a
        dimension and each value is a list of cuboids in that dimension, after
        merging the input cuboid with the existing cuboids.

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
    Calculates the total size of intersections between a given cuboid and multiple
    cuboids stored in a dictionary, considering their orientation and volume. It
    uses the `get_intersection` function to find overlapping volumes and sums them
    up based on the dimension.

    Args:
        cuboids_dict (Dict[str, List[Cuboid]]): Represented as a dictionary where
            each key is a string representing a dimension and each value is a list
            of Cuboid objects.
        next_cuboid (Dict[str, Cuboid]): Represented as a dictionary where keys
            are dimension names and values are lists of Cuboid objects.

    Returns:
        int: The size of the intersection of the next cuboid with all cuboids in
        the dictionary, calculated by summing the volumes of intersecting parts
        with a positive or negative sign depending on the dimension.

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
