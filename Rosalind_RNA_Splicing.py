"""
Problem Title: RNA Splicing
Rosalind ID: SPLC
URL: http://rosalind.info/problems/splc/

Genes are Discontiguous

Figure 1. The elongation of a pre-mRNA by RNAP as it moves down the template strand of DNA.

Figure 2. RNA is identical to the coding strand except for the replacement of thymine with uracil.
In “Transcribing DNA into RNA”, we mentioned that a strand of DNA is copied into a strand of RNA during transcription, but we neglected to mention how transcription is achieved.

In the nucleus, an enzyme (i.e., a molecule that accelerates a chemical reaction) called RNA polymerase (RNAP) initiates transcription by breaking the bonds joining complementary bases of DNA. It then creates a molecule called precursor mRNA, or pre-mRNA, by using one of the two strands of DNA as a template strand: moving down the template strand, when RNAP encounters the next nucleotide, it adds the complementary base to the growing RNA strand, with the provision that uracil must be used in place of thymine; see Figure 1.

Because RNA is constructed based on complementarity, the second strand of DNA, called the coding strand, is identical to the new strand of RNA except for the replacement of thymine with uracil. See Figure 2 and recall “Transcribing DNA into RNA”.

After RNAP has created several nucleotides of RNA, the first separated complementary DNA bases then bond back together. The overall effect is very similar to a pair of zippers traversing the DNA double helix, unzipping the two strands and then quickly zipping them back together while the strand of pre-mRNA is produced.

For that matter, it is not the case that an entire substring of DNA is transcribed into RNA and then translated into a peptide one codon at a time. In reality, a pre-mRNA is first chopped into smaller segments called introns and exons; for the purposes of protein translation, the introns are thrown out, and the exons are glued together sequentially to produce a final strand of mRNA. This cutting and pasting process is called splicing, and it is facilitated by a collection of RNA and proteins called a spliceosome. The fact that the spliceosome is made of RNA and proteins despite regulating the splicing of RNA to create proteins is just one manifestation of a molecular chicken-and-egg scenario that has yet to be fully resolved.

In terms of DNA, the exons deriving from a gene are collectively known as the gene's coding region.

Problem
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample Output
MVYIADKQHVASREAYGHMFKVCA
"""
from parse_fasta import parse


def transcribe(dna):
    """
    Transcribe DNA into RNA
    """
    return dna.replace('T', 'U')


def translate(rna):
    """
    Translate RNA into protein
    """
    codon_table = {
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
    protein = ''
    # take 3-letter codon at a time
    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]
        if codon in codon_table:
            amino_acid = codon_table[codon]
            if amino_acid == 'Stop':
                break
            protein += amino_acid
    return protein


def identify_exons(s, introns):
    """
    Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
    Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
    """
    # 1. Remove all matches of introns from DNA string iteratively
    for intron in introns:
        s = s.replace(intron, '')
    exons = [s]
    # 2. Transcribe the exons into RNA
    rna_exons = [transcribe(exon) for exon in exons]
    # 3. Translate the RNA exons into protein
    protein_exons = [translate(rna_exon) for rna_exon in rna_exons]
    # 4. Concatenate the protein exons
    protein = ''.join(protein_exons)
    # return the protein starting from the start codon
    return protein[protein.index('M'):]


def main():
    file = './txt_files/rosalind_splc.txt'
    seqs = parse(file)
    s = str(seqs[0])
    # print(s)
    introns = seqs[1:]
    # print(introns)
    protein = identify_exons(s, introns)
    print(protein)


if __name__ == '__main__':
    main()
