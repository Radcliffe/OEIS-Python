# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A143823

from functools import cache
def b(n, s):
    if n < 1: return 1
    sn = s + [n]
    m = len(sn)
    return (b(n-1, sn) if m*(m-1)//2 == len(set(sn[i]-sn[j] for i in range(m-1) for j in range(i+1, m))) else 0) + b(n-1, s)
@cache
def a(n): return b(n-1, [n]) + (0 if n==0 else a(n-1))
print([a(n) for n in range(31)]) # _Michael S. Branicky_, Feb 15 2024 after _Alois P. Heinz_

