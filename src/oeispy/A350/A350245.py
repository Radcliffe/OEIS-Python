# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350245

from sympy import integer_nthroot, primerange
def aupto(limit):
    aset, maxp = set(), integer_nthroot(limit**2, 3)[0]
    for p in primerange(3, maxp+1):
        pp = p*p
        for q in primerange(3, min(p-1, limit//pp)+1):
            if (p+1)%q == 0:
                aset.add(pp*q)
    return sorted(aset)
print(aupto(120000)) # _Michael S. Branicky_, Dec 21 2021

