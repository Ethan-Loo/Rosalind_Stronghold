from parse_fasta import parse
seq = parse('./txt_files/rosalind_revp.txt')[0]

Comp_Dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def rev_comp(seq=seq, cd=Comp_Dict):
    r = ''
    for l in seq:
        r = cd[l.upper()]+r
    return r

print(seq)

minimum = 4
maximum = 12
match_list = []
for i in range(minimum, maximum+1):
    for ind, v in enumerate(seq):
        target=seq[ind: ind+i]
        rc=rev_comp(seq = target, cd = Comp_Dict)
        if len(target) >= 4 and target == rc:
            print('match!')
            match_list.append((ind+1, len(target)))

match_list=sorted(list(set(match_list)))
result = ''+'\n'.join(' '.join(map(str, x)) for x in match_list)
print(result)