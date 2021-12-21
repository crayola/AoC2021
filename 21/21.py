from collections import Counter

def update_counters(roll, n_universes, player, universe_count):
    universe_count_new = Counter()
    wins = 0
    for (pos1, sco1), (pos2, sco2) in universe_count.keys():
        pos, sco = (pos1, sco1) if player == 1 else (pos2, sco2)
        newpos = (pos + roll) % 10
        newsco = sco + newpos + 1
        if newsco >= 21:
            wins += n_universes * universe_count[(pos1, sco1), (pos2, sco2)]
        elif player == 1:
            universe_count_new[(newpos, newsco), (pos2, sco2)] = n_universes * universe_count[(pos1, sco1), (pos2, sco2)]
        else:
            universe_count_new[(pos1, sco1), (newpos, newsco)] = n_universes * universe_count[(pos1, sco1), (pos2, sco2)]
    return universe_count_new, wins

if __name__ == '__main__':
    start1, start2 = (3, 7)
    pos1, pos2 = (start1, start2)
    score1, score2 = (0, 0)
    i = 0
    while score1 < 1000 and score2 < 1000:
        pos1 = (pos1 + (i + 1) + (i + 2) + (i + 3)) % 10
        score1 += pos1 + 1
        i += 3
        if score1 < 1000:
            pos2 = (pos2 + (i + 1) + (i + 2) + (i + 3)) % 10
            score2 += pos2 + 1
            i += 3
    print("Part 1:", i * min(score1, score2))
    universe_count = Counter()
    universe_count[(3,0), (7, 0)] += 1
    player = 2
    wins = {1:0, 2:0}
    while universe_count:
        player = 2 if player == 1 else 1
        universe_count_next = Counter()
        for roll, n_universes in [(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]:
            universe_count_new, nwins = update_counters(roll, n_universes, player, universe_count)
            universe_count_next += universe_count_new
            wins[player] += nwins
        universe_count = universe_count_next.copy()
    print("Part 2:", wins[1])