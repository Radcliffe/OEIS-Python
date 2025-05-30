# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364384

from math import gcd
from sympy import integer_nthroot
def A364384(n):
    if n == 1: return 1
    c = 0
    for v in range(0,n):
        for w in range(0,n-v):
            u = n-v-w
            if gcd(u,v,w)==1:
                v2, w2, u2 = v*v, w*(u<<2), u<<1
                if v2+w2>=0:
                    d, r = integer_nthroot(v2+w2,2)
                    if r and not ((d+v)%u2 or (d-v)%u2):
                        c += 1
                        if v>0 and w>0:
                            c += 1
                if v2-w2>=0:
                    d, r = integer_nthroot(v2-w2,2)
                    if r and not((d+v)%u2 or (d-v)%u2):
                        c += 1
                        if v>0 and w>0:
                            c += 1
    return c # _Chai Wah Wu_, Oct 04 2023

