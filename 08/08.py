import numpy as np
from import Counter

def parse_input(file):
    lines = open(file,'r').readlines()
    lines = [x.strip().split(' | ') for x in lines]
    signals_array = np.array([x[0].split() for x in lines])
    output_array = np.array([x[1].split() for x in lines])
    return(signals_array, output_array)

def part_1_sum(output_array):
    output_length_array = np.vectorize(len)(output_array)
    return(
        np.sum(output_length_array == 2, axis=(0, 1)) +
        np.sum(output_length_array == 3, axis=(0, 1)) +
        np.sum(output_length_array == 4, axis=(0, 1)) +
        np.sum(output_length_array == 7, axis=(0, 1))
    )

def decoder(sig_row):
    sig_len = np.vectorize(len)(sig_row)
    decoded = {}
    decoded['a'] = list(set(sig_row[sig_len == 3][0]) - set(sig_row[sig_len == 2][0]))[0]
    fivers = Counter(''.join(sig_row[sig_len == 5])))
    return a

if __name__ == "__main__":
    signals_array, output_array= parse_input("08/input")
    print(part_1_sum(output_array))
    decoder(signals_array[0])