# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A363919

from sympy import factorint
def A363919(n): return n**sum(map(lambda e:e-1,factorint(n).values())) # _Chai Wah Wu_, Jul 18 2023

