# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A046660

from sympy import factorint
def A046660(n): return sum(e-1 for e in factorint(n).values()) # _Chai Wah Wu_, Jul 18 2023

