# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A005383

from sympy import isprime
[n for n in range(3, 5000) if isprime(n) and isprime((n + 1)//2)]
# _Indranil Ghosh_, Mar 17 2017

