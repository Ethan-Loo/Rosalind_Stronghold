def probability(file_name):
    """Takes a .txt file input with three numbers separated by spaces
    and computes Mendelian probability of homozygous dominant factors
    given homozygous dominant, heterozygous,
    and homozygous recessive populations"""
    f = open(file_name, 'r')
    ints = f.readline()
    ints = ints.split(" ")
    k = float(ints[0])
    m = float(ints[1])
    n = float(ints[2])
    tot = k + m + n


    result = (k*(k-1)+(k*m+m*k)+(k*n+n*k)+.75*m*(m-1)+(.5*(m*n)+.5*(n*m)))/(tot*(tot-1))

    return result


print(probability('./txt_files/rosalind_iprb.txt'))
