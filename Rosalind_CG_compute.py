from parse_fasta import parse
CG_list = ()
headers = []
seqs = []
temp = ''
CG_pcts = []

file = './txt_files/rosalind_gc.txt'
seqs, headers = parse(fasta_file=file, return_heads=True)

for seq in seqs:
    CG_pcts.append(round((seq.count('C')+seq.count('G'))/len(seq)*100,6)) # Count CG's and divide by length of sequence

CG_list = list(sorted(zip(headers, CG_pcts), key= lambda x: x[1], reverse= True)) # sort by GC%

print('\n'.join([str(item) for item in CG_list]))
