# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A217565

from sympy import isprime, nextprime, prime
from sympy.ntheory import count_digits
def a(n):
    pn = prime(n); qn = nextprime(pn)
    p, q = 2, 3; c = count_digits((q**pn)*(p**qn))
    while not all(isprime(c[i]) for i in range(10)):
        p, q = q, nextprime(q); c = count_digits((q**pn)*(p**qn))
    return p
print([a(n) for n in range(1, 7)]) # _Michael S. Branicky_, Aug 21 2021

