# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A090706

from math import comb
def A090706(n): return comb(n.bit_length()-1,n.bit_count()-1) if n else 1 # _Chai Wah Wu_, Mar 06 2025

