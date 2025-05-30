# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A138666

from sympy import isprime
from itertools import accumulate
def ok(n): return all(not isprime(s) for s in accumulate(range(n, 0, -1)))
def aupto(nn): return [m for m in range(1, nn+1) if ok(m)]
print(aupto(148)) # _Michael S. Branicky_, Jan 08 2021

