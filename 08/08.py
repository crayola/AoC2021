import numpy as np
from collections import Counter

def parse_input(file):
    lines = open(file,'r').readlines()
    lines = [x.strip().split(' | ') for x in lines]
    signals_array = np.array([x[0].split() for x in lines])
    output_array = np.array([x[1].split() for x in lines])
    return(signals_array, output_array)

def part_1_sum(output_array):
    output_length_array = np.vectorize(len)(output_array)
    return(np.sum(np.isin(output_length_array, [2,3,4,7]), axis=(0, 1)))

def build_decoder(sig_row):
    """
    Builds the decoder dict for a given (1,10) signals row.
    This leverages the observation that if I count the number of patterns in which each segment appears
    (1) in the whole signals row 
    (2) in the signals row where I remove the (easily identifiable) digit 4
    each of the 7 segments has a unique 'signature'. 
    For example:
    - segment 'a' is the only one which appears 8 times both with digit 4 included, and with digit 4 excluded.
    - segment 'b' is the only one which appears 6 times with digit 4 included, and 5 times with digit 4 excluded.
    - etc.
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
    """Given the (1,4) input row and the decoder, returns the corresponding row integer."""
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
