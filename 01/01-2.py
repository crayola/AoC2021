if __name__ == "__main__":
    with open("01/input-0101.txt", "r") as f:
        increases = 0
        l1 = int(f.readline())
        l2 = int(f.readline())
        l3 = int(f.readline())
        while l3:
            l4 = f.readline()
            try:
                l4 = int(l4)
                if l2 + l3 + l4 > l1 + l2 + l3: 
                    increases += 1
            except Exception as e:
                print(e)
            print(l4, l2 + l3 + l4, increases)
            l1 = l2
            l2 = l3
            l3 = l4
            #if increases == 10:
    print(f"Total increases: {increases}")
