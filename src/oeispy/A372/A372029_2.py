# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A372029

# faster for initial segment of sequence
from sympy import factorint, isprime
from itertools import count, islice, combinations_with_replacement as mc
def nd(s): return s == "".join(sorted(s))
def bgen(d): # can't end in 8 or 9
    yield from ("".join(m) for m in mc("1234567", d))
def agen(): # generator of terms
    for d in count(2):
        for s in bgen(d):
            t = int(s)
            if any(s[-1] > c and t%int(c) == 0 for c in "2357"): continue
            if isprime(t): continue
            if nd(s+"".join(str(p)*e for p, e in factorint(t).items())):
                yield t
print(list(islice(agen(), 25))) # _Michael S. Branicky_, Apr 22 2024

