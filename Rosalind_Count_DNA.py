def count(test_string):
    """Counts the number of times each nucleotide occurs in a string of DNA and prints the counts."""
    test_string.upper()
    print(f'{test_string.count("A")} {test_string.count("C")} '
          f'{test_string.count("G")} {test_string.count("T")}')


def main():
    with open('./txt_files/rosalind_dna.txt') as infile:
        test_string = infile.readline()
        count(test_string)

if __name__ == '__main__':
    main()