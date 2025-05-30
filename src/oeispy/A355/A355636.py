# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355636

from sympy import divisor_count
from itertools import count, islice
def agen():
    anm1, an, mink, seen = 1, 1, 2, {1}
    yield 1
    for n in count(2):
        yield an
        k, target, tsum = mink, divisor_count(anm1+an), anm1+an
        while k in seen or k == tsum or divisor_count(k) != target: k += 1
        while mink in seen: mink += 1
        anm1, an = an, k
        seen.add(an)
print(list(islice(agen(), 73))) # _Michael S. Branicky_, Jul 26 2022

