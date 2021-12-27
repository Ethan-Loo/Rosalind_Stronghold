def count(test_string):
    test_string.upper()
    print(f'{test_string.count("A")} {test_string.count("C")} '
          f'{test_string.count("G")} {test_string.count("T")}')


def main():
    with open('./rosalind_dna.txt') as infile:
        test_string = infile.readline()
        count(test_string)

if __name__ == '__main__':
    main()