# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A076621

from sympy import prime, primerange
def aupton(terms):
    primes = list(primerange(3, prime(terms+1)+1))
    return [9] + [((p+q)//2)**2 for p, q in zip(primes[:-1], primes[1:])]
print(aupton(43)) # _Michael S. Branicky_, Sep 16 2021

