# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A132174

from __future__ import division
def A132174(n):
    if n == 1:
        return 1
    if n == 2:
        return 5
    h, m = divmod(n - 3, 5)
    return (382*2**(5*h + m)-10*2**m)//31- 7*h - m -(1 if m==3 else (-1 if m==4 else 2)) # _Chai Wah Wu_, May 17 2017

