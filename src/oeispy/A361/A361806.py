# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A361806

from sympy import primefactors, sieve
def A361806(n):
    primeset = []
    for composites in range (sieve[n]+1, sieve[n+1]):
        for p in primefactors(composites): primeset.append(p)
    return(sum(set(primeset)))

