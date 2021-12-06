import numpy as np
dims = (999, 999)

def parse_input(file):
    lines_raw = open(file, 'r').readlines()
    lines = [x.strip().split(' -> ') for x in lines_raw]
    parsed = [[np.array(y.split(','), 'int') for y in x] for x in lines]
    return(parsed)

def fill_line(line, diagram):
    n_steps = np.max(np.absolute(line[1] - line[0]))
    steps = np.around(np.linspace(line[0], line[1], n_steps+1)).astype(int) # without rounding bad things happen
    for x in steps:
        diagram[int(x[0]), int(x[1])] += 1
    return(diagram)

if __name__ == "__main__":
    lines = parse_input("05/input")
    diagram = np.zeros(dims)
    diagram2 = np.zeros(dims)
    for line in lines:
        diagram = fill_line(line, diagram)
    print(sum(sum(diagram >= 2)))
