# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A052220

from sympy.utilities.iterables import multiset_permutations
def auptodigs(maxdigits):
    alst = []
    for d in range(1, maxdigits+1):
        digset = "0"*(d-1) + "11111122233456"
        for p in multiset_permutations(digset, d):
            if p[0] != '0' and sum(map(int, p)) == 6:
                alst.append(int("".join(p)))
    return alst
print(auptodigs(4)) # _Michael S. Branicky_, Jun 15 2021

