with open('./txt_files/rosalind_rna.txt') as infile:
    line = infile.readline()
    print(line.replace('T','U'))