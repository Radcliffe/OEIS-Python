# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A056008

from math import isqrt
def A056008(n): return (isqrt(m:=1<<n)+1)**2-m # _Chai Wah Wu_, Apr 28 2023

