# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A035105

from math import lcm
from sympy import fibonacci
def A035105(n): return lcm(*(fibonacci(i) for i in range(1,n+1))) # _Chai Wah Wu_, Jul 17 2022

