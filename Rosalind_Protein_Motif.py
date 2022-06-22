from urllib.request import urlopen
import re

encoding = 'utf-8'


def parse_and_find(code=''):
    fasta = urlopen("https://www.uniprot.org/uniprot/" + code + ".fasta").read().decode(encoding)
    seq = "".join(fasta[re.search(r'>sp.*\n', fasta).end():].split())
    # print(code)
    motifs = [m.start(1) + 1 for m in re.finditer(r'(?=(N[^P][ST][^P]))', seq)]
    motifs = " ".join(str(i) for i in motifs)
    if len(motifs) > 0:
        print(code, motifs, sep='\n')
        return
    else:
        return


def main():
    file = './txt_files/rosalind_mprt.txt'
    with open(file) as infile:
        for line in infile:
            parse_and_find(code=line.strip())


if __name__ == '__main__':
    main()
