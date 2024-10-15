import numpy as np
from io import StringIO

def get_pixel(a: np.ndarray, algo):
    """
    extracts a pixel from an image array represented as a binary string, where
    each pixel is encoded as a binary number. It uses the `algo` array to map the
    index of the pixel to its corresponding value.

    Args:
        a (np.ndarray*): Represented as a 2D NumPy array, likely containing pixel
            data, where each element is a binary value.
        algo (List[int]): Used to represent a list of integers where each index
            corresponds to a binary number represented by a 2D NumPy array `a`.

    Returns:
        npndarray|None: The result of indexing into the `algo` array using the
        integer `index` converted from a binary string representation of the
        flattened input array `a`.

    """
    index = int(''.join(a.flatten().astype(str)), 2)
    return algo[index]

def enhance(a, algo, step):
    """
    Applies a specified image enhancement algorithm (`algo`) to a given image (`a`)
    in a 9-pixel neighborhood, padding the image with zeros or ones, depending on
    the step number, and returns the enhanced image.

    Args:
        a (numpy.ndarray): Used as the input image to be processed.
        algo (Union[str, List[str], int, List[int], Dict[str, int], Dict[int,
            str]]): Used as an argument to the `get_pixel` function, which is not
            shown in the provided code.
        step (int): Used to determine the initialization method of the 2D array
            `b`. If `step` is odd, `b` is initialized with zeros, otherwise it is
            initialized with ones.

    Returns:
        numpyndarray: A 2D array of size `a.shape[0] + 2` by `a.shape[1] + 2` with
        pixel values enhanced according to the specified algorithm.

    """
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
