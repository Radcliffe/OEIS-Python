# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371381

from math import isqrt
def A371381(n): return (n<<1)*(n-1)+1+(q:=n+isqrt(5*n**2)>>1)*(q-(n-1<<1)) # _Chai Wah Wu_, Mar 21 2024

