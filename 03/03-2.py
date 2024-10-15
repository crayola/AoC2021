def get_ith_bit(input, i, gas):
    """
    Calculates the value of the `i`-th bit in a binary number represented as a
    string within a list of input values. It sums the occurrences of '1' at the
    `i`-th position, then determines the value of the `i`-th bit based on the sum
    and the type of gas.

    Args:
        input (List[Dict[str, str]]): Composed of dictionaries where each dictionary
            represents a binary number as a string with keys being the bit positions
            and values being the corresponding bit values ("0" or "1").
        i (int): Used to index into the binary strings in the input list, effectively
            selecting a specific position to examine for each string.
        gas (str): Used to determine the value of the ith bit based on the sum of
            the ith bits in the input list. It can be either "o2" or "co2",
            indicating whether to return the bit that is most or least common in
            the input list.

    Returns:
        str: Either "1" or "0", representing the ith bit of the oxygen or CO2
        rating, depending on the input parameter 'gas'.

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