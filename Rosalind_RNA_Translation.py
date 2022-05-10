def translate(seq, codon_table):
    seq = seq.lower().replace('\n', '').replace(' ', '')
    peptide = ''

    for i in range(0, len(seq), 3):
        codon = seq[i: i+3]
        amino_acid = codon_table.get(codon, '*')
        if amino_acid != '*':
            peptide += amino_acid
        else:
            break
    return peptide

def main():
    bases = "ucag"
    codons = [a + b + c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids))
    seq=''
    with open('./txt_files/rosalind_prot.txt') as infile:
        for line in infile:
            seq += line
        print(seq)
        pep = translate(seq, codon_table)
    print(pep)

if __name__ == '__main__':
    main()