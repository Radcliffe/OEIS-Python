# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350661

from sympy import prod, primefactors
from functools import lru_cache
rad = lambda n: prod(primefactors(n))
@lru_cache()
def a(n):
    if n == 1: return 1
    return a(rad(n)-1)+n
print([a(i) for i in range(1, 100)])

