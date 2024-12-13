import numpy as np
dims = (999, 999)

def parse_input(file):
    """
    Reads a file, removes newline characters and splits each line into two parts,
    converts each part into an array of integers separated by commas, and returns
    the resulting list of lists.

    Args:
        file (str): Expected to be a path to a file containing input data.

    Returns:
        List[List[npndarray]]: A list of lists of NumPy arrays, where each inner
        list represents a line of input and each array represents a point in 2D space.

    """
    lines_raw = open(file, 'r').readlines()
    lines = [x.strip().split(' -> ') for x in lines_raw]
    parsed = [[np.array(y.split(','), 'int') for y in x] for x in lines]
    return(parsed)

def fill_line(line, diagram):
    """
    Increases the value at each point along a line in a 2D diagram, effectively
    drawing the line by incrementing the count at each point by one.

    Args:
        line (List[Tuple[int, int]]): Represented by two points in a 2D coordinate
            system, (line[0] and line[1]), which define the line to be filled.
        diagram (numpy.ndarray): Used to accumulate the count of points along a
            line in a 2D space.

    Returns:
        numpyndarray: The updated `diagram` with increased values at each point
        `x` in the `steps` sequence, representing the line's density.

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
