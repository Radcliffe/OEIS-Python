# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A064144

from math import factorial
from sympy import divisor_count
def A064144(n): return divisor_count(factorial(n)+1) # _Chai Wah Wu_, Oct 20 2023

