# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A368885

from sympy import factorint
def A368885(n): return 1<<sum(1 for e in factorint(n).values() if e==2) # _Chai Wah Wu_, Jan 09 2024

