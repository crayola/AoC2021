if __name__ == "__main__":
    with open("01/input-0101.txt", "r") as f:
        increases = 0
        l = int(f.readline())
        while l:
            l1 = f.readline()
            try:
                l1 = int(l1)
                if l1 > l: 
                    increases += 1
            except Exception as e:
                print(e)
            print(l, increases)
            l = l1
            #if increases == 10:
    print(f"Total increases: {increases}")
