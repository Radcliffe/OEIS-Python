# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356327

from sympy import fibonacci
def A356327(n): return sum(fibonacci(-a)*int(b) for a, b in enumerate(bin(n)[:1:-1],start=1)) # _Chai Wah Wu_, Aug 31 2022

