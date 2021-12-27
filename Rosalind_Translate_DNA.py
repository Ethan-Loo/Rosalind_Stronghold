original = 'ATCG'
comp = 'TAGC'

# seq = 'AAAACCCGGT'
with open('./rosalind_revc.txt') as infile:
    seq = infile.readline()
    complement = seq.translate(seq.maketrans(original, comp))[::-1]
print(complement)