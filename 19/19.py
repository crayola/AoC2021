import re
import numpy as np
from io import StringIO
import itertools


def get_all_rotations(scanner):
    """Get 24 sets of beacon coordinates corresponding to every possible rotation"""
    Rx90 = np.array([[1,0,0], [0,0,-1], [0,1,0]])
    Ry90 = np.array([[0,0,1], [0,1,0], [-1,0,0]])
    Rz90 = np.array([[0,-1,0], [1,0,0], [0,0,1]])
    rotations = [scanner]
    for i in range(3):
        rotations += [rot @ Rx90 for rot in rotations]
        rotations += [rot @ Ry90 for rot in rotations]
        rotations += [rot @ Rz90 for rot in rotations]
    set_rotations_bytes = set([rot.tobytes() for rot in rotations]) # numpy arrays not hashable
    rotations = [np.frombuffer(x, dtype=int).reshape(-1,3) for x in set_rotations_bytes]
    return rotations

def convert_scanner(scanner1, scanner2):
    """Try to match the beacons detected by scanner 2 and those from scanner 1. 
    Return: 
    - scanner2 beacon coordinates as seen from scanner1
    - the coordinates of scanner2 as seen from scanner 1"""
    scanner2_rotations = get_all_rotations(scanner2)
    shift = np.zeros((scanner1.shape[0] * scanner2.shape[0], 3))
    for scan2rot in scanner2_rotations:
        for i, beacon1 in enumerate(scanner1):
            startindex = i * scanner2.shape[0] 
            endindex = (i+1) * scanner2.shape[0] 
            shift[startindex:endindex] = scan2rot - beacon1
        unq, count = np.unique(shift, axis=0, return_counts=True)
        if (count >= 12).any(): # assume we have a match if at least 12 beacons seem to be at the same locations
            scanner2 = scan2rot - unq[count>=12]
            return scanner2, unq[count>=12]
    return None, None

def manhattan(a: np.ndarray):
    combinations = list(itertools.combinations(range(a.shape[0]),2))
    max_manhattan = 0
    for x1, x2 in combinations:
        max_manhattan = int(max([np.sum(np.abs(a[x1] - a[x2])), max_manhattan]))
    return max_manhattan

if __name__ == "__main__":
    scanners_txt = re.split("\n*--- scanner \d* ---\n", open('19/input').read())[1:]
    scanners = list(enumerate([np.loadtxt(StringIO(s), delimiter=',', dtype=int) for s in scanners_txt]))
    all_beacons = scanners[0][1] # scanner 0 is the reference scanner
    scanners = scanners[1:]
    all_shift = []
    while scanners: # find matching beacons and rotate scanners iteratively until all scanners are matched
        for i, scanner in scanners:
            converted, shift = convert_scanner(all_beacons, scanner)
            if converted is not None:
                all_shift += [shift]
                scanners = [(j, scanner) for (j, scanner) in scanners if i != j]
                all_beacons = np.unique(np.vstack([all_beacons, converted]), axis=0)
    print("Part 1:", all_beacons.shape[0])
    print("Part 2:", manhattan(np.vstack(all_shift)))
