# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A351889

from functools import lru_cache
from math import lcm
from itertools import count
from sympy import factorint
@lru_cache(maxsize=None)
def A351889_T(n,k): # computes the period of the n-step Fibonacci sequence mod k
    if len(fs := factorint(k)) <= 1:
        a = b = (0,)*(n-1)+(1 % k,)
        s = 1 % k
        for m in count(1):
            b, s = b[1:] + (s,), (s + s - b[0]) % k
            if a == b:
                return m
    else:
        return lcm(*(A351889_T(n,p**e) for p, e in fs.items()))

