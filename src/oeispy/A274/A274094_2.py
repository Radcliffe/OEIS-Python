# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A274094

from math import isqrt
def A274094(n): return m if (m:=isqrt(n<<3)+1>>1)&1 else -m # _Chai Wah Wu_, Nov 05 2024

