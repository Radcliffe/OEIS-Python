# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A052882

from math import factorial
from sympy.functions.combinatorial.numbers import stirling
def A052882(n): return n*sum(factorial(k)*stirling(n-1,k) for k in range(n)) # _Chai Wah Wu_, Apr 15 2023

