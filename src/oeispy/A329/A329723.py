# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A329723

from sympy import lucas
def A329723(n): return 1 if n <= 1 else lucas(n-2) # _Chai Wah Wu_, Feb 04 2022

