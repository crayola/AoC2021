import numpy as np
from io import StringIO

def get_pixel(a: np.ndarray, algo):
    index = int(''.join(a.flatten().astype(str)), 2)
    return algo[index]

def enhance(a, algo, step):
    if step % 2 == 1:
        b = np.zeros((a.shape[0] + 4, a.shape[1] + 4), dtype=int)
    else:
        b = np.ones((a.shape[0] + 4, a.shape[1] + 4), dtype=int)
    b[2:-2, 2:-2] = a
    c = np.zeros((a.shape[0] + 2, a.shape[1] + 2), dtype=int)
    for i in range(1, b.shape[0] - 1):
        for j in range(1, b.shape[1] - 1):
            pix9 = (b[(i-1):(i+2), (j-1):(j+2)])
            c[i-1,j-1] = get_pixel(pix9, algo)
    return c

if __name__ == "__main__":
    algo, image = open('20/input').read().replace('.', '0').replace('#', '1').split('\n\n')
    image = np.genfromtxt(StringIO(image), delimiter=1, dtype=int)
    print("Part 1:", np.sum(enhance(enhance(image, algo, 1), algo, 2), axis=(0,1)))
    for i in range(50):
        image = enhance(image, algo, i+1)
    print("Part 2:", np.sum(image, axis=(0,1)))
