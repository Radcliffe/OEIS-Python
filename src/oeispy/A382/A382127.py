# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A382127

from sympy import isprime
from itertools import count
def a(n):
    return next(p for p in count(2) if isprime(p) and len(set(str(p)))==n and '0' not in str(p) and all(isprime(2*p*int(d)+1) for d in set(str(p))))

