# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A046000

def ok(k, n): return sum(map(int, str(k**n))) == k
def a(n):
    d, lim = 1, 1
    while lim < n*9*d: d, lim = d+1, lim*10
    return next(k for k in range(lim, 0, -1) if ok(k, n))
print([a(n) for n in range(63)]) # _Michael S. Branicky_, Jul 06 2022

