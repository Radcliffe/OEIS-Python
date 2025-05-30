# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A380347

from sympy import isprime
from itertools import count, islice
def agen(): # generator of terms
    yield 1
    an1, an, aset, m = 1, 3, {1}, 7
    for n in count(2):
        yield an
        aset.add(an)
        s2, str2 = an1 + an, str(an1) + str(an)
        k = next(j for j in count(m, 2) if j not in aset and j%10 != 5 and isprime(s2+j) and isprime(int(str2+str(j))))
        an1, an = an, k
        while m in aset or m%2 == 5: m += 2
print(list(islice(agen(), 61))) # _Michael S. Branicky_, Jan 22 2025

