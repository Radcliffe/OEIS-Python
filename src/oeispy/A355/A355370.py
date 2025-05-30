# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355370

def ok(k, n): return sum(map(int, str(k**n)))%k==0
def row(n):
    d, lim = 1, 1
    while lim < n*9*d: d, lim = d+1, lim*10
    yield from [k for k in range(1, lim+1) if ok(k, n)]
print([an for n in range(9) for an in row(n)]) # _Michael S. Branicky_, Jul 06 2022

