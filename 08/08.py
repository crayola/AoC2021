import numpy as np
from collections import Counter

def parse_input(file):
    """
    reads a file and returns two arrays: `signals_array` contains the input signals,
    while `output_array` contains the corresponding output values.

    Args:
        file (open file.): file to be parsed and is used to read its contents into
            the function.
            
            	File is an open file handle returned by the `open` function in read
            mode (`'r'`). The `readlines()` method reads and returns all the lines
            of the file as a list of strings. Each line is split into two parts
            using the split() method, and the resulting list of tuples is assigned
            to the `signals_array` and `output_array` variables.
            
            	Therefore, `file` has the following properties:
            
            		- File name: The name of the file being read.
            		- Mode: The mode in which the file is opened (read in this case).
            		- Lines: A list of strings representing all the lines of the file.

    Returns:
        `numpy` array.: a tuple of two arrays: `signals_array` and `output_array`.
        
        		- `signals_array`: A NumPy array containing the input signals. Each
        element in the array is a list of two values, where the first value
        represents the signal name and the second value represents the signal value.
        		- `output_array`: A NumPy array containing the output values for each
        signal. Each element in the array is a list of two values, where the first
        value represents the output name and the second value represents the output
        value.

    """
    lines = open(file,'r').readlines()
    lines = [x.strip().split(' | ') for x in lines]
    signals_array = np.array([x[0].split() for x in lines])
    output_array = np.array([x[1].split() for x in lines])
    return(signals_array, output_array)

def part_1_sum(output_array):
    """
    computes the sum of elements in an output array that have lengths 2, 3, 4, or
    7, along both axis(0) and axis(1).

    Args:
        output_array (ndarray.): 2D array containing the lengths of the parts in
            the problem.
            
            		- The type of `output_array` is `np.ndarray`.
            		- The shape of `output_array` is `(N, M)`, where N and M are the
            lengths of the two arrays being processed.
            		- The values in `output_array` are integers between 0 and 8, inclusive.
            		- The array has a total of 4 unique values: 2, 3, 4, and 7.
            		- The array is sorted in ascending order.

    Returns:
        int: a tensor of lengths of arrays in the input `output_array`.

    """
    output_length_array = np.vectorize(len)(output_array)
    return(np.sum(np.isin(output_length_array, [2,3,4,7]), axis=(0, 1)))

def build_decoder(sig_row):
    """
    takes a signal row as input and builds a dictionary to identify the unique
    signature of each segment in the row based on the number of occurrences of
    each digit, including and excluding digit 4.

    Args:
        sig_row (int): 10-element signals row that is to be processed and decoded
            using the function.

    Returns:
        dict: a dictionary containing unique signatures for each segment in the
        signals row.

    """
    sig_len = np.vectorize(len)(sig_row)
    decoder = {}
    count_all = Counter(''.join(sig_row))
    count_no_4 = Counter(''.join(sig_row[sig_len!=4]))
    for k in "abcdefg":
        to_match = (count_all[k], count_no_4[k])
        if to_match == (8, 8):
            decoder[k] = "a"
        elif to_match == (6, 5):
            decoder[k] = "b"
        elif to_match == (8, 7):
            decoder[k] = "c"
        elif to_match == (7, 6):
            decoder[k] = "d"
        elif to_match == (4, 4):
            decoder[k] = "e"
        elif to_match == (9, 8):
            decoder[k] = "f"
        elif to_match == (7, 7):
            decoder[k] = "g"
    return(decoder)

def decode(output, decoder):
    """
    takes an output row and a decoder as input, returning the corresponding integer
    value. It iterates over each digit in the output row, using the decoder to
    determine the corresponding integer value for each segment of the digit. The
    resulting integer is then returned.

    Args:
        output (list): 1x4 matrix of digits that are to be decoded.
        decoder (str): 16-digit binary code that is decoded by the function.

    Returns:
        int: an integer representing the decoded digit.

    """
    decoded_digits = ""
    for digit in output:
        decoded_digit_segments = set()
        for char in digit:
            decoded_digit_segments.add(decoder[char])
        if decoded_digit_segments == set("abcefg"):
            decoded_digits += "0"
        elif decoded_digit_segments == set("cf"):
            decoded_digits += "1"
        elif decoded_digit_segments == set("acdeg"):
            decoded_digits += "2"
        elif decoded_digit_segments == set("acdfg"):
            decoded_digits += "3"
        elif decoded_digit_segments == set("bcdf"):
            decoded_digits += "4"
        elif decoded_digit_segments == set("abdfg"):
            decoded_digits += "5"
        elif decoded_digit_segments == set("abdefg"):
            decoded_digits += "6"
        elif decoded_digit_segments == set("acf"):
            decoded_digits += "7"
        elif decoded_digit_segments == set("abcdefg"):
            decoded_digits += "8"
        elif decoded_digit_segments == set("abcdfg"):
            decoded_digits += "9"
    return(int(decoded_digits))


if __name__ == "__main__":
    signals_array, output_array= parse_input("08/input")
    print(part_1_sum(output_array)) # part 1
    decoded_output = []
    for i in range(signals_array.shape[0]):
        decoder = build_decoder(signals_array[i,:])
        decoded_output += [decode(output_array[i], decoder)]
    print(sum(decoded_output)) # part 2
