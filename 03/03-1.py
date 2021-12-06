if __name__ == "__main__":
    with open("./03/input", 'r') as f:
        l = f.readline()
        running_sum = [0] * 12
        while l:
            bytetup = l.strip()
            bytetup = [1 if int(x) else -1 for x in bytetup]
            l = f.readline()
            running_sum = [x[0] + x[1] for x in zip(running_sum, bytetup)]
    print(running_sum)
    gamma_list = [1 if x>0 else 0 for x in running_sum]
    epsilon_list = [1 if x<0 else 0 for x in running_sum]
    gamma = int(''.join(map(str, gamma_list)), 2)
    epsilon = int(''.join(map(str, epsilon_list)), 2)

    print(gamma, epsilon, gamma * epsilon)