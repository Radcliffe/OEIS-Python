# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A210256

from math import isqrt
def A210256(n): return ((m:=isqrt((n+1<<2)+1)+1>>1)*(m-1)>>1)+sum((n+1)//k for k in range(1,(n+1)//m+1))-((r:=isqrt((n<<2)+1)+1>>1)*(r-1)>>1)-sum(n//k for k in range(1,n//r+1)) # _Chai Wah Wu_, Oct 31 2023

