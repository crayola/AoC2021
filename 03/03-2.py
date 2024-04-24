def get_ith_bit(input, i, gas):
    """
    calculates and returns the ith bit (0-based) of a given binary input based on
    the gas type "o2" or "co2".

    Args:
        input (str): 1D array of integers that contains the original gas measurements.
        i (int): 0-based index of the bit to be calculated within the input string.
        gas (str): gas being measured, which determines whether the result of the
            calculation is a 1 or a 0 for that particular bit.

    Returns:
        int: a single bit representing the result of an integer calculation based
        on input values.

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