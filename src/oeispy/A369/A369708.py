# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A369708

from collections import Counter
from sympy import prime
def A369708(n):
    c = {0:1}
    for i in range(2,n+1):
        p, d = prime(i), Counter(c)
        for k in c:
            d[k+p] += c[k]
        c = d
    return max(c.values()) # _Chai Wah Wu_, Jan 31 2024

