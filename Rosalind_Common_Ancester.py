seq_list = []
temp = ''

# Open file and read in sequences
with open('./txt_files/rosalind_cons.txt') as infile:
    for line in infile:
        if line.startswith('>'):
            seq_list.append(temp)
            temp = ''
        else:
            temp += line.strip('\r\n')
    if len(temp) > 0:
        seq_list.append(temp)
    seq_list = seq_list[1:]
seq_list.sort()


# Initialize list with 0's
def _list_initiate(seq_list):
    pos_count = []
    for i in seq_list[0]:
        pos_count.append(0)
    return pos_count


# Count nucleotides
def count_nuc(nuc, seq_list=[]):
    pos_count = _list_initiate(seq_list=seq_list)
    for i in range(0, len(seq_list)):
        for index, v in enumerate(seq_list[i]):
            count = pos_count[index]
            if v == nuc:
                count += 1
                pos_count[index] = count
    print(nuc + ':', *pos_count)
    return pos_count


def main():
    A = count_nuc(nuc='A', seq_list=seq_list)
    C = count_nuc(nuc='C', seq_list=seq_list)
    G = count_nuc(nuc='G', seq_list=seq_list)
    T = count_nuc(nuc='T', seq_list=seq_list)

    nuc_dict = {'A': A, 'C': C, 'G': G, 'T': T}

    profile_lst = []
    for num, v in enumerate(A):
        count_lst = []
        for key in nuc_dict.keys():
            count_lst.append(nuc_dict[key][num])
        profile_lst.append(max(count_lst))

    consensus = ''
    for num, v in enumerate(profile_lst):
        used = False
        for key, value in nuc_dict.items():
            if used:
                pass
            elif v == value[num]:
                consensus += key
                used = True
    print(consensus)


if __name__ == '__main__':
    main()
