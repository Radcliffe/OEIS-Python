# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A113574

from sympy import isprime
def a(n): return 1 if n<2 else int(str(a(n - 1)) + "2") if isprime(n) else int(str(a(n - 1)) + "4")
print([a(n) for n in range(1, 51)]) # _Indranil Ghosh_, Apr 12 2017

