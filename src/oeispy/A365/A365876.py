# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A365876

from math import gcd
def A365876(n):
    if n == 1: return 1
    c = 0
    for v in range(1,n+1>>1):
        u = n-(v<<1)
        if gcd(u,v)==1:
            v2, u2 = v*v, v*(u<<2)
            if v2+u2 >= 0:
                c +=1
            if v2-u2 >= 0:
                c +=1
    return c # _Chai Wah Wu_, Oct 04 2023

