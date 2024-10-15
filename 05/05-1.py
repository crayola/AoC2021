import numpy as np
dims = (999, 999)

def parse_input(file):
    """
    Reads a file, strips and splits each line into two parts, converts each part
    into a list of integers, and returns a list of lists containing these integer
    values.

    Args:
        file (str): Expected to specify the path to a text file containing raw
            input data.

    Returns:
        List[List[nparray]]: A 2D list of NumPy arrays, where each inner list
        represents a line from the input file and each NumPy array represents a
        pair of coordinates.

    """
    lines_raw = open(file, 'r').readlines()
    lines = [x.strip().split(' -> ') for x in lines_raw]
    parsed = [[np.array(y.split(','), 'int') for y in x] for x in lines]
    return(parsed)

def fill_line(line, diagram):
    """
    Increases the count in a 2D diagram at each point along a line segment, where
    the line segment is divided into a specified number of steps, and the count
    at each point is incremented by 1.

    Args:
        line (List[Tuple[int, int]]): Represented as a list of two points in a 2D
            space, where each point is a tuple of two integers representing the x
            and y coordinates.
        diagram (Any): Modified in-place to represent the frequency of line segments
            in a diagram, where each value at a position in the diagram corresponds
            to the count of lines passing through that point.

    Returns:
        ndarray: An updated version of the input `diagram` with incremented values
        at each point on the line.

    """
    n_steps = np.max(np.absolute(line[1] - line[0]))
    steps = np.around(np.linspace(line[0], line[1], n_steps+1)).astype(int) # without rounding bad things happen
    for x in steps:
        diagram[x[0], x[1]] += 1
    return(diagram)

if __name__ == "__main__":
    lines = parse_input("05/input")
    diagram = np.zeros(dims)
    for line in lines:
        diagram = fill_line(line, diagram)
    print(sum(sum(diagram >= 2)))
