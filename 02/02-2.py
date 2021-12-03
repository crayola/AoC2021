if __name__ == "__main__":
    h = 0
    d = 0
    a = 0
    with open("02/input-02.txt", 'r') as f:
        l = f.readline()
        while l:
            direction, amount = l.split()
            if direction == "up":
                a -= int(amount)
            if direction == "down":
                a += int(amount)
            if direction == "forward":
                h += int(amount)
                d += a * int(amount)
            l = f.readline()
    print(h, d, h*d)
