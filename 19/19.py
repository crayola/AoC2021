import re
import numpy as np
from io import StringIO
import itertools


def get_all_rotations(scanner):
    Rx90 = np.array([[1,0,0], [0,0,-1], [0,1,0]])
    Ry90 = np.array([[0,0,1], [0,1,0], [-1,0,0]])
    Rz90 = np.array([[0,-1,0], [1,0,0], [0,0,1]])
    rotations = [scanner]
    for i in range(3):
        rotations += [rot @ Rx90 for rot in rotations]
        rotations += [rot @ Ry90 for rot in rotations]
        rotations += [rot @ Rz90 for rot in rotations]
    rotations = [np.frombuffer(x, dtype=int).reshape(-1,3)
        for x in set([rot.tobytes() for rot in rotations])]
    return rotations


    Rx = [np.linalg.matrix_power() for i in [0,1,2,3]]
    Ry = [np.linalg.matrix_power() for i in [0,1,2,3]]
    Rz = [np.linalg.matrix_power(np.array(), i) for i in [0,1,2,3]]
    rotations_matrices = itertools.product(Rx, Ry, Rz)
    Rlist = set([x[0] @ x[1] @ x[2] for x in rotations_matrices])
    return [scanner @ rot for rot in Rlist]


def convert_scanner(scanner1, scanner2):
    scanner2_rotations = get_all_rotations(scanner2)
    diff = np.zeros((scanner1.shape[0] * scanner2.shape[0], 3))
    for scan2rot in scanner2_rotations:
        for i, beacon1 in enumerate(scanner1):
            startindex = i * scanner2.shape[0] 
            endindex = (i+1) * scanner2.shape[0] 
            diff[startindex:endindex] = scan2rot - beacon1
        unq, count = np.unique(diff, axis=0, return_counts=True)
        if (count >= 3).any():
            print("got it:", np.max(count))
            scanner2 = scan2rot - unq[count>=3]
            return scanner2, unq[count>=3]
    return None, None

def manhattan(arr):
    combinations = list(itertools.combinations(range(arr.shape[0]),2))
    current_max = 0
    for x1, x2 in combinations:
        current_max = max([np.sum(np.abs(arr[x1] - arr[x2])), current_max])
    return current_max

#manhattan(np.array([[1,2,3],[4,5,6],[7,8,9]]))
#manhattan(np.array([[1,2,3],[4,5,6],[70,8,9]]))

if __name__ == "__main__":
    scanners_txt = re.split("\n*--- scanner \d* ---\n", open('19/input').read())[1:]
    scanners = [np.loadtxt(StringIO(s), delimiter=',', dtype=int) for s in scanners_txt]
    print(scanners[0:2])
    #print(get_all_rotations(scanners[0])[1])
    #print(len(get_all_rotations(scanners[0])))
    all_beacons = scanners[0]
    for i in range(1, len(scanners)):
        converted, _ = convert_scanner(all_beacons, scanners[i])
        if converted is not None:
            print("Converted scanner", i)
            all_beacons = np.unique(np.vstack([all_beacons, converted]), axis=0)
        else:
            print("Could not convert scanner", i)
    all_diff = []
    for i in range(1, len(scanners)):
        converted, diff = convert_scanner(all_beacons, scanners[i])
        if converted is not None:
            all_diff += [diff]
            print("Converted scanner", i)
            all_beacons = np.unique(np.vstack([all_beacons, converted]), axis=0)
        else:
            print("Could not convert scanner", i)
    print(all_beacons.shape)
    print(manhattan(np.vstack(all_diff)))