from parse_fasta import parse

def main():

    file = './txt_files/rosalind_lcsm.txt'
    seqs = parse(fasta_file=file)

    #Get shortest of DNA strings
    index = seqs.index(min(seqs, key=len))

    motif = 'A'
    shortest = seqs[index]

    #cycle over the DNA string letters
    for i in range(len(shortest)):
        n = 0
        present = True
        while present:
            #cycle inside over all other DNA strings and if it's present in there considered a motif and length gets increased by 1
            for each in seqs:
                if shortest[i:i+n] not in each or n>1000:
                    present = False
                    break
            if present:
                motif = max(shortest[i:i+n], motif, key=len)
            n += 1
    print(motif)

if __name__ == '__main__':
    main()
