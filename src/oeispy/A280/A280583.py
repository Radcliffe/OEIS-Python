# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A280583

from math import isqrt
from sympy import divisor_count
def A280583(n): return (lambda m:(isqrt(m) if (c:=divisor_count(m)) & 1 else 1)*m**(c//2))(divisor_count(n)) # _Chai Wah Wu_, Jun 25 2022

