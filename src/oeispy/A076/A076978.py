# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A076978

from sympy import sieve as p, primefactors
def A076978(n):
    result = 1
    for composites in range(p[n]+1, p[n+1]):
        for primefactor in primefactors(composites):
            if result % primefactor != 0: result *= primefactor
    return result # _Karl-Heinz Hofmann_, May 30 2022

