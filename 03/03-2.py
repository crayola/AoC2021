def get_ith_bit(input, i, gas):
    """
    Calculates the `ith` bit of a binary string `input` based on a given gas type
    ("o2" or "co2"). It sums the bits at position `i` in all strings, then determines
    the `ith` bit of the most/least common string(s) accordingly.

    Args:
        input (List[str]): Expected to contain a list of binary strings.
        i (int): Used to index the bits in the input strings. It represents the
            position of the bit to be determined.
        gas (str | "o2" | "co2"): Used to determine the bit to select based on the
            sum of the ith bits in the input list. It can be either "o2" for Oxygen
            or "co2" for Carbon Dioxide.

    Returns:
        str: Either the bit value ("0" or "1") at the specified index `i` in the
        binary representation of the life support rating for oxygen ("o2") or
        carbon dioxide ("co2") based on the given `input` and `gas` type.

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