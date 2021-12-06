import numpy as np
dims = (999, 999)

def parse_input(file):
    lines_raw = open(file, 'r').readlines()
    lines = [x.strip().split(' -> ') for x in lines_raw]
    parsed = [[np.array(y.split(','), 'int') for y in x] for x in lines]
    return(parsed)

def fill_line(line, diagram):
    if line[0][0] == line[1][0]:
        minrange = min(line[0][1], line[1][1])
        maxrange = max(line[0][1], line[1][1])
        for x in range(minrange, maxrange+1):
            diagram[line[0][0], x] += 1
    elif line[0][1] == line[1][1]:
        minrange = min(line[0][0], line[1][0])
        maxrange = max(line[0][0], line[1][0])
        for x in range(minrange, maxrange+1):
            diagram[x, line[0][1]] += 1
    else:
        minrangex = min(line[0][0], line[1][0])
        maxrangex = max(line[0][0], line[1][0])
        minrangey = min(line[0][1], line[1][1])
        maxrangey = max(line[0][1], line[1][1])
        if minrangex == line[0][0]:
            is_ascending = False if line[0][1] > line[1][1] else True
        elif minrangex == line[1][0]:
            is_ascending = True if line[0][1] > line[1][1] else False
        if is_ascending:
            j = minrangey
            for x in range(minrangex, maxrangex+1):
                diagram[x, j] += 1
                j+=1
        if not is_ascending:
            j = maxrangey
            for x in range(minrangex, maxrangex+1):
                diagram[x, j] += 1
                j-=1
    return(diagram)


if __name__ == "__main__":
    lines = parse_input("05/input-05.txt")
    diagram = np.zeros(dims)
    for line in lines:
        diagram = fill_line(line, diagram)
    print(sum(sum(diagram >= 2)))