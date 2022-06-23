#! /usr/bin/env python

def Calc_Offspring(file_name):
    """This function calculates the expected number of offspring for a population with the dominant trait."""
    f = open(file_name, 'r')
    ints = f.readline()
    ints = ints.split(" ")
    dominant_offspring = [1, 1, 1, 3 / 4, 2 / 4, 0] #offspring for each possible parent
    ints = [float(i) for i in ints]

    result = sum([v * dominant_offspring[i] for i, v in enumerate(ints)]) * 2 #multiply by 2 because each parent is represented by 2

    return result


print(Calc_Offspring('./txt_files/rosalind_iev.txt'))
