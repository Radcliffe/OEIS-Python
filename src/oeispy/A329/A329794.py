# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A329794

from sympy.ntheory.primetest import is_square
def positive_square(n): return n > 0 and is_square(n)
def box(i, j):
    si = str(i); sj = str(j); m = max(len(si), len(sj))
    si, sj = si.zfill(m), sj.zfill(m)
    return int("".join([str(abs(int(si[k])-int(sj[k]))) for k in range(m)]))
def a(n):
    k = 1
    while not positive_square(box(k, n)): k += 1
    return k
print([a(n) for n in range(1, 66)]) # _Michael S. Branicky_, Aug 20 2021

