"""
Problem Title: Enumerating k-mers Lexicographically
Rosalind ID: LEXF
URL: http://rosalind.info/problems/lexf/

Organizing Strings
When cataloguing a collection of genetic strings, we should have an established system by which to organize them. The standard method is to organize strings as they would appear in a dictionary, so that "APPLE" precedes "APRON", which in turn comes before "ARMOR".

Problem
Assume that an alphabet A has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).

Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in A.

Given: A collection of at most 10 alphabet defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of alphabet in the English alphabet).

Sample Dataset
A C G T
2

Sample Output
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT

"""

from itertools import permutations
from itertools import repeat


# Create a list of all possible permutations of the alphabet in lexicographic order given the alphabet as a list and length of the string
def lexicographic(alphabet, n):
    permutaion = sorted(set(permutations([x for item in alphabet for x in repeat(item, n)], n)))
    for item in permutaion:
        print(''.join(item))


def main():
    with open('./txt_files/rosalind_lexf.txt', 'r') as f:
        alphabet = f.readline().strip().split()
        n = int(f.readline().strip())
    lexicographic(alphabet, n)


if __name__ == '__main__':
    main()
