def meet_target(velocity, target):
    x = 0
    y = 0
    step = 0
    while x <= target[0][1] and y >= target[1][0]:
        step += 1
        print (step, x, y)
        x += velocity[0]
        y += velocity[1]
        velocity = (velocity[0] - (velocity[0] > 0), velocity[1] - 1)
        if (x >= target[0][0] and x <= target[0][1] and 
            y >= target[1][0] and y <= target [1][1]):
            return "Hit!"
    return "No hit :-("


if __name__ == '__main__':
    target = [(88, 125), (-157, -103)]
    #x=88..125, y=-157..-103

    #final_x = 1 + 2 + .. + vel_x
    #= (vel_x) * (vel_x + 1) / 2

    #vel_x = 

    print(meet_target((15, 156), target))