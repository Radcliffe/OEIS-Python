# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A143804

from math import isqrt
def A143804(n): return 3*((m:=n<<1)-(k:=isqrt(m))-int(m>=k*(k+1)+1))-2 # _Chai Wah Wu_, Aug 01 2022

