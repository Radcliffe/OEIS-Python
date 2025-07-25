# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A360573

from math import comb, isqrt
from sympy import integer_nthroot
def A056557(n): return (k:=isqrt(r:=n+1-comb((m:=integer_nthroot(6*(n+1), 3)[0])-(n<comb(m+2, 3))+2, 3)<<1))-((r<<2)<=(k<<2)*(k+1)+1)
def A333516(n): return (r:=n-1-comb((m:=integer_nthroot(6*n, 3)[0])+(n>comb(m+2, 3))+1, 3))-comb((k:=isqrt(m:=r+1<<1))+(m>k*(k+1)), 2)+1
def A360010(n): return (m:=integer_nthroot(6*n, 3)[0])+(n>comb(m+2, 3))
def A360573(n):
    a = (a2:=integer_nthroot(24*n, 4)[0])+(n>comb(a2+2, 4))+3
    j = comb(a-1,4)-n
    b, c, d = A360010(j+1)+2, A056557(j)+2, A333516(j+1)
    return (1<<a)-(1<<b)-(1<<c)-(1<<d)-1 # _Chai Wah Wu_, Dec 18 2024

