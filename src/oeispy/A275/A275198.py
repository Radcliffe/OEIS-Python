# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A275198

from math import comb, isqrt
from sympy.ntheory.modular import crt
def A275198(n):
    w, c = n-((r:=(m:=isqrt(k:=n+1<<1))-(k<=m*(m+1)))*(r+1)>>1), 1
    d = int(not ~r & w)
    while True:
        r, a = divmod(r,7)
        w, b = divmod(w,7)
        c = c*comb(a,b)%7
        if r<7 and w<7:
            c = c*comb(r,w)%7
            break
    return crt([7,2],[c,d])[0] # _Chai Wah Wu_, May 01 2025

