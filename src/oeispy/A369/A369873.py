# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A369873

from collections import Counter
from sympy import divisors
def A369873(n):
    c = {0:1}
    for d in divisors(n,generator=True):
        b = Counter()
        for j in c:
            a = c[j]
            b[j+d] += a
            b[j-d] += a
        c = b
    return c[0] # _Chai Wah Wu_, Feb 05 2024

