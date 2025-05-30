# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A302294

from __future__ import division
from sympy import divisors, divisor_count
def A302294(n):
    s = set()
    for i in range(1,(n+3)//2):
        for j in divisors(i):
            for k in divisors(n-i):
                if j != k:
                    s.add((min(j,k),max(j,k)))
    return 3*divisor_count(n)+2*len(s)-1 # _Chai Wah Wu_, May 21 2018

