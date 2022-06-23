def fib_count(n=None, k=None):
    """This function performs the fibonacci sequence and returns the number of
    children that will be born in the next n generations."""
    rabbit_pairs=[1,1,]
    for i in range(1,n-1):
        mature_rabs = i-1
        children = (rabbit_pairs[mature_rabs])*3+rabbit_pairs[i]
        print(f'generation {i+3}, children {children}')
        rabbit_pairs.append(children)
    return rabbit_pairs


def main():
    n = 32
    k = 3
    fib_list = fib_count(n,k)
    print(fib_list)

if __name__ == '__main__':
    main()