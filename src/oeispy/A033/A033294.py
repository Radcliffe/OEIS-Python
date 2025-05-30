# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A033294

from math import isqrt
from itertools import count, islice
def sqr(n): return isqrt(n)**2 == n
def agen():
    yield from (k*k for k in count(1) if k%10 and sqr(int(str(k*k)[::-1])))
print(list(islice(agen(), 36))) # _Michael S. Branicky_, May 21 2022

