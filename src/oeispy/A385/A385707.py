# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A385707

from sympy.utilities.iterables import partitions
from sympy import isprime
res = []
for n in range(22):
    for p in partitions(n):
        for i, f in p.items():
            if not isprime(i) or f>1:
                break
        else:
            res.extend(list(p.keys()))
print(res)

