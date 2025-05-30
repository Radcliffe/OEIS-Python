# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A162734

from sympy import isprime, primerange
def nontwins(N):
    return [p for p in primerange(1, N+1) if not (isprime(p-2) or isprime(p+2))]
def auptont(N): # all terms where the larger non-twin <= N
    nt = nontwins(N)
    return [sum((-1)**(j+1)*j for j in range(nt[i], nt[i+1]+1)) for i in range(len(nt)-1)]
print(auptont(565)) # _Michael S. Branicky_, Nov 30 2021

