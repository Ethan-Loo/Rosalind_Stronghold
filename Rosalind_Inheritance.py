import math

hetero=28
domin=26
recess=17

total = hetero+domin+recess

def doublefactorial(n):
    """This function will return the double factorial of a number using a recursive function"""
    if (n == 0 or n == 1):
        return 1;
    return n * doublefactorial(n - 2);

# Driver Code
print("Double factorial is",
      doublefactorial(total));

total_combos = math.factorial(total)/doublefactorial(total)

print(f'total possible combinations is {total_combos}')