import numpy as np

def parse_input(file):
    lines = open(file,'r').readlines()
    lines = [x.strip().split(' | ')[1] for x in lines]
    wordslen = np.array([[len(y) for y in x.split()] for x in lines])
    #lines[1] = lines[1].split()
    return(wordslen)

if __name__ == "__main__":
    lines = parse_input("08/input")
    print(np.sum(lines == 3, axis=(0, 1)))
    print(np.sum(lines == 4, axis=(0, 1)))
    print(np.sum(lines == 8, axis=(0, 1)))
    print(
        np.sum(lines == 2, axis=(0, 1)) +
        np.sum(lines == 3, axis=(0, 1)) +
        np.sum(lines == 4, axis=(0, 1)) +
        np.sum(lines == 7, axis=(0, 1))
    )