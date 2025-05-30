# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A065582

from sympy import isprime
def a(n):
    pow, end, i = 10**n, 10**n-1, 1
    while i%10 == 9 or not isprime(i*pow + end): i += 1
    return i*pow + end
print([a(n) for n in range(1, 20)]) # _Michael S. Branicky_, Jul 30 2022

