# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A000603

from math import isqrt
def A000603(n): return (m:=n<<1)+sum(isqrt(k*(m-k)) for k in range(1,n))+1 # _Chai Wah Wu_, Jul 18 2024

