# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A332028

from math import isqrt
def A332028(n): return (k:=(r:=isqrt(m:=n+1<<1))+int((m<<2)>(r<<2)*(r+1)+1)-1)*(6*n-2-k*(k+3))//6+(isqrt(n<<3)+1>>1)+n if n>1 else 3 # _Chai Wah Wu_, Jun 07 2025

