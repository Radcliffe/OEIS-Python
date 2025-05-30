# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377661

from math import comb, isqrt, factorial
def A377661(n):
    a = (m:=isqrt(k:=n+1<<1))-(k<=m*(m+1))
    b = n-comb(a+1,2)
    fa, fb = factorial(a), factorial(b)
    return comb(a,b)*sum(fa//(fb*factorial(j-b)) for j in range(b,a+1)) # _Chai Wah Wu_, Nov 12 2024

