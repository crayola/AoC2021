def meet_target(velocity, target):
    left, right, bottom, top = target
    h_vel, v_vel = velocity
    x, y = (0, 0)
    while x <= right and y >= bottom:
        x += h_vel
        y += v_vel
        h_vel = h_vel + (h_vel > 0)
        v_vel = v_vel - 1
        if (x >= left and x <= right and 
            y >= bottom and y <= top):
            return True
    return False

if __name__ == '__main__':
    target = (88, 125, -157, -103) # my input
    _, right, bottom, _ = target
    print("Part 1:", bottom * (bottom + 1) // 2)
    hits = []
    for h_vel in range(right + 1):
        for v_vel in range(bottom - 1, -bottom):
            if meet_target((h_vel, v_vel), target):
                hits += [(h_vel, v_vel)]
    print("Part 2:", len(hits))
