from collections import Counter

def grow_chain_1(polymer):
    """
    Extends a polymer chain by one unit at a time. It iterates through the chain,
    appending the current unit and the next unit's pair value from a predefined
    'rules' dictionary, effectively growing the chain according to these rules.

    Args:
        polymer (str): Represented as a sequence of characters, typically a string
            of monomers, which are the building blocks of the polymer.

    Returns:
        str: A polymer chain grown from the input polymer by applying the rules
        in the dictionary `rules`.

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
    """
    Calculates the difference between the counts of the most common and least
    common elements in a given polymer. It uses the `Counter` class to count the
    occurrences of each element and returns the absolute difference between the
    two counts.

    Args:
        polymer (str): Represented as a string of characters that make up the polymer.

    Returns:
        int: The difference between the counts of the most common element and the
        least common element in the input polymer.

    """
    polycount = Counter(polymer).most_common()
    return polycount[0][1] - polycount[-1][1]

def grow_chain_2(polymer: Counter):
    """
    Applies a set of rules to a polymer chain, represented as a Counter object,
    to simulate its growth over time. It iteratively applies each rule to each
    unit in the chain, incrementing the counts of new units and decrementing the
    count of the original unit.

    Args:
        polymer (Counter*): Represented as a dictionary where keys are monomer
            pairs and values are their respective counts in the polymer chain.

    Returns:
        Dict[str,int]: A Counter object representing the updated polymer chain
        after applying the growth rules.

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
    Calculates the difference between the most common and least common element
    counts in a polymer after removing specified units. It takes a polymer counter,
    a first unit, and a last unit as input and returns half of this difference.

    Args:
        polymer_counter (Counter*): Expected to be a dictionary-like object where
            keys are pairs of characters and values are their respective counts.
        first (str): Used to increment the count of the first character of the
            most frequent unit pair in the polymer.
        last (str): Specified as the last unit to be counted in the polymer.

    Returns:
        int: The difference between the counts of the two most common polymer units
        divided by 2.

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

