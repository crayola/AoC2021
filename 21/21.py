from collections import Counter

def update_counters(roll, player, universe_count):
    n_universes = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}[roll]
    universe_count_new = Counter()
    wins = 0
    for (pos1, sco1), (pos2, sco2) in universe_count.keys():
        position, score = (pos1, sco1) if player == 1 else (pos2, sco2)
        new_position = (position + roll) % 10
        new_score = score + new_position + 1
        if new_score >= 21:
            wins += n_universes * universe_count[(pos1, sco1), (pos2, sco2)]
        elif player == 1:
            universe_count_new[(new_position, new_score), (pos2, sco2)] = (
                n_universes * universe_count[(pos1, sco1), (pos2, sco2)]
            )
        else:
            universe_count_new[(pos1, sco1), (new_position, new_score)] = (
                n_universes * universe_count[(pos1, sco1), (pos2, sco2)]
            )
    return universe_count_new, wins

if __name__ == '__main__':
    # Part 1
    pos1, pos2 = (3, 7)
    sco1, sco2 = (0, 0)
    i = 0
    while sco1 < 1000 and sco2 < 1000:
        pos1 = (pos1 + (i + 1) + (i + 2) + (i + 3)) % 10
        sco1 += pos1 + 1
        i += 3
        if sco1 < 1000:
            pos2 = (pos2 + (i + 1) + (i + 2) + (i + 3)) % 10
            sco2 += pos2 + 1
            i += 3
    print("Part 1:", i * min(sco1, sco2))

    # Part 2
    universe_count = Counter()
    universe_count[(3, 0), (7, 0)] = 1
    player = 2
    wins = {1:0, 2:0}
    while universe_count:
        player = 2 if player == 1 else 1
        universe_count_next = Counter()
        for roll in range(3, 10):
            universe_count_new, nwins = update_counters(roll, player, universe_count)
            universe_count_next += universe_count_new
            wins[player] += nwins
        universe_count = universe_count_next.copy()
    print("Part 2:", wins[1])
