# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355237

from itertools import count
from sympy import factorint
def A355237(n):
    m = 2
    for k in count(2):
        c = False
        for p in (f:=factorint(k)):
            if (q:= p & 3)==3 and f[p]&1:
                break
            elif q == 1:
                c = True
        else:
            if c or f.get(2,0)&1:
                if k-m == n:
                    return m
                m = k # _Chai Wah Wu_, Jul 01 2022

