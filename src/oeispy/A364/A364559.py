# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364559

from sympy import factorint, primepi
def A364559(n): return sum(1<<primepi(p)+i for i, p in enumerate(factorint(n, multiple=True),-1))+1-n # _Chai Wah Wu_, Jul 29 2023

