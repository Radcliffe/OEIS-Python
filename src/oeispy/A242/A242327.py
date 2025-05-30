# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A242327

import sympy
from sympy.ntheory import isprime, nextprime
n=2
while True:
    n1=n+2
    n2=n**3+2
    n3=n**5+2
    n4=n**7+2
    ##.Check if n1, n2, n3 and n4 are also primes
    if all(isprime(x) for x in [n1, n2, n3, n4]):
        print(n, ", ", n1, ", ", n2, ", ", n3, ", ", n4)
    n=nextprime(n)

