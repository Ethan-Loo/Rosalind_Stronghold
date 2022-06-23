def Rabbit(k,m):
    """This function will return the number of rabbits that will be alive after m months. """
    import copy
    rabbits = [0 for i in range(m)]
    rabbits[-1] = 1
    new = copy.deepcopy(rabbits) #deepcopy to avoid changing the original list
    for i in range(k-1):
        new[:-1] = rabbits[1:]
        new[-1] = sum(rabbits[:-1])
        rabbits = copy.deepcopy(new)
    return sum(rabbits),rabbits

def main():
    k = 93
    m = 20

    total, rabbits = Rabbit(k=k, m=m)
    print(total, rabbits)

if __name__ == '__main__':
    main()