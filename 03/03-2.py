def get_ith_bit(input, i, gas):
    """
    takes an input string, an index `i`, and a gas type `gas`. It calculates the
    bit at position `i` in the input string based on the value of `gas`. The bit
    is returned as a string "1" or "0".

    Args:
        input (str): 1D array of gas concentrations to be processed by the function.
        i (int): 0-based index of the bit to be checked in the input string.
        gas (str): gas being measured, with values of "o2" or "co2", and determines
            the output of the `ith_bit` variable.

    Returns:
        str: a single bit representation of the input gas, determined by the sum
        of the binary digits.

    """
    sumith = sum([1 if x[i]=="1" else -1 for x in input])
    if gas == "o2":
        ith_bit = "1" if sumith >= 0 else "0"
    elif gas == "co2":
        ith_bit = "0" if sumith >= 0 else "1"
    return ith_bit

def filter(input, i, gas):
    return [x for x in input if x[i] == get_ith_bit(input, i, gas)]

if __name__ == "__main__":
    with open("./03/input", 'r') as f:
        l = f.readline()
        parsed_input = []
        while l:
            bytetup = l.strip()
            parsed_input += [bytetup]
            l = f.readline()
    remaining_bits_o2 = parsed_input
    n_o2 = 2
    i = 0
    while n_o2 > 1:
        remaining_bits_o2 = filter(remaining_bits_o2, i, "o2")
        i += 1
        n_o2 = len(remaining_bits_o2)
        print(n_o2)
        print(remaining_bits_o2)
    remaining_bits_co2 = parsed_input
    n_co2 = 2
    i = 0
    while n_co2 > 1:
        remaining_bits_co2 = filter(remaining_bits_co2, i, "co2")
        i += 1
        n_co2 = len(remaining_bits_co2)
        print(n_co2)
        print(remaining_bits_co2)
    oxygen_generator_rating =  int(remaining_bits_o2[0], 2)
    co2_scrubber_rating = int(remaining_bits_co2[0], 2)
    print(oxygen_generator_rating * co2_scrubber_rating)