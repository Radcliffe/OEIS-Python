# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A061201

from math import isqrt
from sympy import integer_nthroot
def A061201(n): return (m:=integer_nthroot(n,3)[0])**3+3*sum(-(s:=isqrt(r:=n//i))**2+(sum(r//k for k in range(1,s+1))<<1)-sum(n//(i*j) for j in range(1,m+1)) for i in range(1,m+1)) # _Chai Wah Wu_, Oct 23 2023

