# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350173

from sympy import prime
def A350173(n): return prime(n)**(n%2+1) # _Chai Wah Wu_, Dec 19 2021

