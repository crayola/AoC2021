def meet_target(velocity, target):
    x, y = (0, 0)
    while x <= target[0][1] and y >= target[1][0]:
        x += velocity[0]
        y += velocity[1]
        velocity = (velocity[0] - (velocity[0] > 0), velocity[1] - 1)
        if (x >= target[0][0] and x <= target[0][1] and 
            y >= target[1][0] and y <= target [1][1]):
            return True
    return False

if __name__ == '__main__':
    target = [(88, 125), (-157, -103)] # my input
    print("Part 1:", target[1][0] * (target[1][0] + 1) // 2)
    hits = []
    for x in range(target[0][1] + 1):
        for y in range(target[1][0] - 1, -target[1][0]):
            if meet_target((x,y), target):
                hits += [(x,y)]
    print("Part 2:", len(hits))
