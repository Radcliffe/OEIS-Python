# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A181133

from math import isqrt
def A181133(n): return n+(isqrt((n<<3)+1)-1>>1) # _Chai Wah Wu_, Feb 10 2023

