# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A338086

from gmpy2 import digits
def A338086(n): return int(''.join(d*2 for d in digits(n,3)),3) # _Chai Wah Wu_, May 07 2022

