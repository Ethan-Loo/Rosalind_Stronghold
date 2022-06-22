from math import factorial as fact

file = './txt_files/rosalind_lia.txt'
with open(file) as infile:
    inputs = infile.readline()
    print(inputs)
# Parse the numbers from the infile
k, N = int(inputs[0]), int(inputs[2:])
P = 2 ** k

# Use a binomial distribution function to estimate the probability given the inputs from the file
Probability = 0
for i in range(N, P + 1):
    prob = (fact(P) / (fact(i) * fact(P - i))) * (0.25 ** i) * (0.75 ** (P - i))
    Probability += prob

print(round(Probability, 3))
