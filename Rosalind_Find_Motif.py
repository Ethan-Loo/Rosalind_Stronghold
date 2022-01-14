import re

with open('./rosalind_subs.txt') as infile:
    seq = infile.readline().strip()
    motif = infile.readline().strip()

loci=set()
# print(seq[1:].find(motif))

for i, v in enumerate(seq):
    # print(seq[i:])
    # print(seq[i:].find(motif)+i)
    # loci.add(seq[i:].find(motif)+i)
    if re.search(motif, seq[i:]) != None:
        # print(re.search(motif, seq[i:]).start()+i)
        loci.add(re.search(motif, seq[i:]).start()+i+1)

print(sorted(loci))