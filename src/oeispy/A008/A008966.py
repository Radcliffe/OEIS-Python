# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A008966

from sympy import factorint
def A008966(n): return int(max(factorint(n).values(),default=1)==1) # _Chai Wah Wu_, Apr 05 2023

