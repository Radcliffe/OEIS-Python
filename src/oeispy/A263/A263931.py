# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A263931

from math import comb
from sympy import primorial
def A263931(n): return comb(m:=n<<1,n)*primorial(n,nth=False)//primorial(m,nth=False) if n else 1 # _Chai Wah Wu_, Sep 07 2022

