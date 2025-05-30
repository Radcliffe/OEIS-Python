# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A230105

from math import prod
from collections import Counter
def b(n): return n + prod(map(int, str(n)))
def aupto(n):
    c = Counter(b(m) for m in range(n+1))
    return [k for k in range(n+1) if c[k] == 1]
print(aupto(185)) # _Michael S. Branicky_, Jan 09 2023

