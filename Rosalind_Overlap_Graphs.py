from parse_fasta import parse

file='./txt_files/rosalind_grph.txt'
seqs, heads = parse(fasta_file=file, return_heads=True)

def find_adj(seqs=[], headers=[], seq_len=1):
    """This function will find all adjacent sequences of length seq_len in the list of sequences."""
    for indx1, seq in enumerate(seqs):
        v = seq[-seq_len:]
        for ind2, seq2 in enumerate(seqs):
            w = seq2[:seq_len]
            if v == w and indx1 != ind2:
                print(headers[indx1],headers[ind2])


find_adj(seqs=seqs, headers=heads, seq_len=3)