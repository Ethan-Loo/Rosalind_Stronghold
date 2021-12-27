with open('./rosalind_rna.txt') as infile:
    line = infile.readline()
    print(line.replace('T','U'))