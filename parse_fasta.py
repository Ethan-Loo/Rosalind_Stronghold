def parse(fasta_file='', return_heads=False):
    """This function will parse .txt and .fasta files in standard header
    and sequence format. Headers and sequences are stored in separate lists
    By default, only sequences are returned"""
    fasta_file=fasta_file
    headers = []
    seqs = []
    temp = ''
    with open(fasta_file) as infile:
        for line in infile:
            if line.startswith('>'):
                seqs.append(temp)
                headers.append(line.strip('>').strip('\r\n'))
                temp = ''
            else:
                temp += line.strip('\r\n')
        if len(temp) > 0:
            seqs.append(temp)
        seqs = seqs[1:]
    # print(seqs)
    if return_heads:
        return seqs, headers
    else:
        return seqs