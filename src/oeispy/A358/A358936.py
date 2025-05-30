# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358936

from sympy import totient as phi
from itertools import count, islice
def f(n): # function we wish to "balance"
    return phi(n)
def agen(): # generator of terms
    s, sset, i = [0, f(1), f(1)+f(2)], set(), 3
    for k in count(2):
        target = s[k-1] + s[k]
        while s[-1] < target:
            fi = f(i); nexts = s[-1] + fi; i += 1
            s.append(nexts); sset.add(nexts)
        if target in sset: yield k
print(list(islice(agen(), 17))) # _Michael S. Branicky_, Dec 07 2022

