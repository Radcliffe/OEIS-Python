# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A280581

from math import isqrt
from sympy import divisor_count, divisor_sigma
def A280581(n): return (lambda m:isqrt(m)**c if (c:=divisor_count(m)) & 1 else m**(c//2))(divisor_sigma(n)) # _Chai Wah Wu_, Jun 25 2022

