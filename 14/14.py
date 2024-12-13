from collections import Counter

def grow_chain_1(polymer):
    """
    Applies given rules to a polymer chain by iterating over each pair of adjacent
    characters. If a pair matches a rule, the corresponding new character is added
    to the chain. The function returns the updated polymer chain.

    Args:
        polymer (Any): A string representing the current state of the polymer chain.

    Returns:
        str: A modified version of the input polymer, where each pair of adjacent
        characters is replaced with the corresponding rule from the `rules`
        dictionary, if applicable.

    """
    new_polymer = ''
    for i in range(len(polymer) - 1):
        c1 = polymer[i]
        c2 = polymer[i+1]
        new_polymer += c1
        if c1 + c2 in rules:
            new_polymer += rules[c1 + c2]
    new_polymer += polymer[-1]
    return new_polymer

def get_score_1(polymer):
    polycount = Counter(polymer).most_common()
    return polycount[0][1] - polycount[-1][1]

def grow_chain_2(polymer: Counter):
    """
    Applies a set of rules to a polymer chain, incrementing counts of new pairs
    and decrementing counts of the original pairs by the number of occurrences of
    each pair.

    Args:
        polymer (Counter): Represented as a dictionary where keys are the units
            of the polymer and values are their respective counts.

    Returns:
        Dict[str,int]: A Counter object representing the updated polymer chain
        after applying the given rules.

    """
    new_polymer = polymer.copy()
    for i in polymer:
        if i in rules:
            to_remove = polymer[i]
            new_polymer[i[0] + rules[i]] += polymer[i]
            new_polymer[rules[i] + i[1]] += polymer[i]
            new_polymer[i] -= to_remove 
    return new_polymer

def get_score_2(polymer_counter: Counter, first, last):
    """
    Calculates the difference between the counts of the most and least common
    elements in a polymer, with two additional counts added for the first and last
    elements.

    Args:
        polymer_counter (Counter): Presumably a collection of polymer pairs and
            their respective counts.
        first (str): Used as a key to increment the count of the first character
            in each polymer pair in the `polymer_counter`.
        last (str): Used to specify the last unit in the polymer chain.

    Returns:
        int: The difference between the two most common elements in the polymer
        and the least common element, divided by 2.

    """
    polymer_count = Counter()
    for p, c in polymer_counter.items():
        polymer_count[p[0]] += c
        polymer_count[p[1]] += c
    polymer_count[first] += 1
    polymer_count[last] += 1
    polycount = polymer_count.most_common()
    return (polycount[0][1] - polycount[-1][1]) // 2

if __name__ == '__main__':
    input = open('14/input').read().strip().split('\n\n')
    polymer = input[0]
    rules = dict([(x.split(' -> ')) for x in input[1].strip().split('\n')])
    for i in range(10):
        polymer = grow_chain_1(polymer)
    print("Part 1:", get_score_1(polymer))
    polymer = input[0]
    polymer_counter = Counter([x + y for x,y in zip(polymer, polymer[1:])])
    for i in range(40):
        polymer_counter = grow_chain_2(polymer_counter)
    print("Part 2:", get_score_2(polymer_counter, polymer[0], polymer[-1]))

