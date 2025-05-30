# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A118596

from sympy import integer_log
from gmpy2 import digits
def A118596(n):
    if n == 1: return 0
    y = 5*(x:=5**integer_log(n>>1,5)[0])
    return int((s:=digits(n-x,5))+s[-2::-1] if n<x+y else (s:=digits(n-y,5))+s[::-1]) # _Chai Wah Wu_, Jun 14 2024

