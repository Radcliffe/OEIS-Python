# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A192273

from sympy import divisors
import numpy as np
A192273 = []
for n in range(3,10**3):
    d = [2*x for x in divisors(n) if n > 2*x and n % (2*x)] + \
        [x for x in divisors(2*n-1) if n > x >=2 and n % x] + \
        [x for x in divisors(2*n+1) if n > x >=2 and n % x]
    s, dmax = sum(d), max(d)
    if not s % 2 and 2*dmax <= s:
        d.remove(dmax)
        s2, ld = int(s/2-dmax), len(d)
        z = np.zeros((ld+1,s2+1),dtype=int)
        for i in range(1,ld+1):
            y = min(d[i-1],s2+1)
            z[i,range(y)] = z[i-1,range(y)]
            z[i,range(y,s2+1)] = np.maximum(z[i-1,range(y,s2+1)],z[i-1,range(0,s2+1-y)]+y)
            if z[i,s2] == s2:
                A192273.append(n)
                break
# _Chai Wah Wu_, Aug 19 2014

