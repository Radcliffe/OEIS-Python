# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355324

from sympy import fibonacci, lucas
def A355324(n): return fibonacci(n+2)+lucas(n+1)>>1 # _Chai Wah Wu_, Aug 08 2022

