# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A147771

from gmpy2 import isqrt_rem
def A147771(n):
    i, j = isqrt_rem(n**n)
    return int(i+int(4*(j-i) >= 1)) # _Chai Wah Wu_, Aug 16 2016

