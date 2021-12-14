from collections import Counter

from numpy import poly

def grow_chain_1(polymer):
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
    new_polymer = polymer.copy()
    for i in polymer:
        if i in rules:
            to_remove = polymer[i]
            new_polymer[i[0] + rules[i]] += polymer[i]
            new_polymer[rules[i] + i[1]] += polymer[i]
            new_polymer[i] -= to_remove 
    return new_polymer

def get_score_2(polymer_counter: Counter):
    polymer_count = Counter()
    for p, c in polymer_counter.items():
        polymer_count[p[0]] += c
        polymer_count[p[1]] += c
    polycount = polymer_count.most_common()
    return polycount[0][1] - polycount[-1][1]


if __name__ == '__main__':
    input = open('14/mini_input').read().strip().split('\n\n')
    polymer = input[0]
    rules = dict([(x.split(' -> ')) for x in input[1].strip().split('\n')])
    print(polymer, rules)
    for i in range(4):
        polymer = grow_chain_1(polymer)
    print("Part 1:", get_score_1(polymer))
    input = open('14/mini_input').read().strip().split('\n\n')
    polymer = input[0]
    polymer_counter = Counter([x + y for x,y in zip(polymer, polymer[1:])])
    for i in range(4):
        polymer_counter = grow_chain_2(polymer_counter)
        print(polymer_counter)
    print(polymer_counter)
    print(polymer_counter.most_common())
    print(get_score_2(polymer_counter))

