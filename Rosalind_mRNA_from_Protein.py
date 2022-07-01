'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Inferring mRNA from Protein
Rosalind ID: MRNA
Rosalind #: 017
URL: http://rosalind.info/problems/mrna/

Pitfalls of Reversing Translation

When researchers discover a new protein, they would like to infer the strand of mRNA from which this protein could have been translated, thus allowing them to locate genes associated with this protein on the genome.
Unfortunately, although any RNA string can be translated into a unique protein string, reversing the process yields a huge number of possible RNA strings from a single protein string because most amino acids correspond to multiple RNA codons (see the RNA Codon Table).
Because of memory considerations, most data formats that are built into languages have upper bounds on how large an integer can be: in some versions of Python, an "int" variable may be required to be no larger than 231−1231−1, or 2,147,483,647. As a result, to deal with very large numbers in Rosalind, we need to devise a system that allows us to manipulate large numbers without actually having to store large numbers.
Problem
For positive integers aa and nn, aa modulo nn (written amodnamodn in shorthand) is the remainder when aa is divided by nn. For example, 29mod11=729mod11=7 because 29=11×2+729=11×2+7.
Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that aa and bb are congruent modulo nn if amodn=bmodnamodn=bmodn; in this case, we use the notation a≡bmodna≡bmodn.
Two useful facts in modular arithmetic are that if a≡bmodna≡bmodn and c≡dmodnc≡dmodn, then a+c≡b+dmodna+c≡b+dmodn and a×c≡b×dmodna×c≡b×dmodn. To check your understanding of these rules, you may wish to verify these relationships for a=29a=29, b=73b=73, c=10c=10, d=32d=32, and n=11n=11.
As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

Sample Dataset
MA
Sample Output
12
'''

encoding = 'utf-8'

# create a dictionary of codons and their corresponding amino acids
codons = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def possible_sequences(sequence):
    '''
    Returns the number of possible RNA sequences from which the protein could have been translated.
    '''
    codon_freq = _codon_frequency()
    n = codon_freq['Stop']
    # for each amino acid multiply by the number of codons for that amino acid
    for amino_acid in sequence:
        n *= codon_freq[amino_acid]
    return n % 1000000  # return the modulo 1,000,000 of the number of possible RNA sequences


def _codon_frequency():
    '''
    Returns a dictionary of codon frequencies.
    '''
    f = {}
    for codon in codons:
        f[codons[codon]] = 0
    for codon in codons:
        f[codons[codon]] += 1
    return f


def main():
    # read the protein sequence from the input file
    with open('./txt_files/rosalind_mrna.txt') as f:
        protein = f.readline().strip()
    print(possible_sequences(protein))  # print the number of possible RNA sequences


if __name__ == '__main__':
    main()
