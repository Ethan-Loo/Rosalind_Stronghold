with open('./txt_files/rosalind_hamm.txt') as infile:
    original = infile.readline()
    mutant = infile.readline()
hamm = 0

for ind, nuc in enumerate(original):
    if nuc != mutant[ind]:
        hamm +=1
print(hamm)