from parse_fasta import parse
CG_list = ()
headers = []
seqs = []
temp = ''
CG_pcts = []
# with open('./rosalind_gc.txt') as infile:
#     for line in infile:
#         if line.startswith('>'):
#             seqs.append(temp)
#             headers.append(line.strip('>').strip('\r\n'))
#             temp = ''
#         else:
#             temp += line.strip('\r\n')
#     if len(temp) > 0:
#         seqs.append(temp)
#     seqs = seqs[1:]
# print(seqs)

file = './txt_files/rosalind_gc.txt'
seqs = parse(fasta_file=file)

for seq in seqs:
    CG_pcts.append(round((seq.count('C')+seq.count('G'))/len(seq)*100,6))

CG_list = list(sorted(zip(headers, CG_pcts), key= lambda x: x[1], reverse= True))
print('\n'.join([str(item) for item in CG_list]))

