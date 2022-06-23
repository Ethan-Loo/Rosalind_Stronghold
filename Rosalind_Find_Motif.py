import re

with open('./txt_files/rosalind_subs.txt') as infile:
    seq = infile.readline().strip()
    motif = infile.readline().strip()

loci = set() # Set to store all locations of motif in seq


for i, v in enumerate(seq):
    if re.search(motif, seq[i:]) != None:
        loci.add(re.search(motif, seq[i:]).start()+i+1) # +1 to account for 0-indexing if motif is found

print(sorted(loci))
