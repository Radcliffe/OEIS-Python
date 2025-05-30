# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367619

from functools import cache
from sympy.ntheory.factor_ import digits
def comma_parent(n, base=3): # A367618(n)
    y = digits(n, base)[1]
    x = (n-y)%base
    k = n - y - base*x
    return k if k > 0 else -1
@cache
def a(n):
    cp = comma_parent(n)
    if cp <= 0: return n
    return a(cp)
print([a(n) for n in range(1, 88)])

