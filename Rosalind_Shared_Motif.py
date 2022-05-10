import re
import itertools
import multiprocessing as mp
from parse_fasta import parse

file= '../DELETE_ME2.txt'

seqs = parse(fasta_file=file)

def find_motifs(seqs=seqs):
    lens=[]
    prelim_mots=[]

    for ind, seq in enumerate(seqs):
        lens.append(len(seq))
        max_len=min(lens)
        print(seq)
        prelim_mots.extend([seq[:i] for i in range(1,max_len+1) if len(seq[:i])>1] or seq!='')
        prelim_mots.extend([seq[i:] for i in range(1,max_len+1) if len(seq[:i])>1 or seq[:1]!=''])
        prelim_mots.extend([seq[i:-i] for i in range(1,max_len+1) if len(seq[:i])>1 or seq[:1]!=''])
    # print(prelim_mots)

    prelim_mots=set(prelim_mots)
    to_del=['','A','T','C','G']
    prelim_mots.difference_update(to_del)
    print(f'Set starts here: -----\n'
          f'{prelim_mots}')
    # print(prelim_mots)
    motifs={}
    count_lst=[]
    # for mot in prelim_mots:
    count=itertools.count(0)
        # print(mot)
    count_lst=[sum(map(lambda mot : re.findall(mot,seq), prelim_mots)) for seq in seqs]
    print(count_lst)
    # motifs=dict(zip([mot for mot in prelim_mots],count_lst))
    # for mot in prelim_mots:
    #     for seq in seqs:
    #         count_lst.append(seq.count(mot))
    # print(count_lst)
    #         if re.findall(mot,seq):
    #             # print('\t'+seq, seq.find(mot), re.findall(mot,seq))
    #             #
    #             next(count),seq
    #             print('\t',count)
    # count_lst.append(count)
    # motifs[mot]=count
    # print(motifs,max(count_lst),sep='\n')
    # print(motifs.values())
    # print(list(motifs.keys())[list(motifs.values()).index(max(count_lst))])



def main():
    find_motifs(seqs=seqs)
    # pool = mp.Pool(mp.cpu_count())
    # print(mp.cpu_count())
    # result = pool.map(find_motifs(seqs=seqs),seqs)

    # process = mp.Process(target=find_motifs(),args=seqs)
    # process.start()

if __name__ == '__main__':
    main()