# Description: Given a list of rational numbers, find their product.
# Sample Input : 3
#                1 2
#                3 4
#                10 6
# Sample Output : 5 8
from fractions import Fraction
from functools import reduce

def product(fracs):
    # Reduce function is filled in with multiplication operator
    t = reduce(lambda x, y : x * y, fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    # fracs represents the list of functions taken in by the input
    fracs = []
    # For each input, store the results in the fracs array
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    # Use the product funciton as the challenge requires
    result = product(fracs)
    # Output results
    print(*result)