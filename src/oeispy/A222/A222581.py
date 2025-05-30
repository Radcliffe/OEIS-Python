# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A222581

from itertools import groupby
def f(s, k):
    return s[:2] if k==4 else (s[1]*(k>=5)+s[0]*(k%5) if k<9 else s[0]+s[2])
def r(n):
    m, c, x, i = n//1000, (n%1000)//100, (n%100)//10, n%10
    return "M"*m + f("CDM", c) + f("XLC", x) + f("IVX", i)
def afull():
    return [len(list(g)) for k, g in groupby("".join(r(i) for i in range(1, 4000)))]
print(afull()[:90]) # _Michael S. Branicky_, Mar 03 2024

