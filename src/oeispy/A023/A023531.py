# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A023531

from math import isqrt
def A023531(n): return int((k:=n+1<<1)==(m:=isqrt(k))*(m+1)) # _Chai Wah Wu_, Nov 09 2024

