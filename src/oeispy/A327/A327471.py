# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A327471

from sympy import totient, divisors
def A327471(n): return (1<<n)-(sum((sum(totient(d)<<k//d-1 for d in divisors(k>>(~k&k-1).bit_length(),generator=True))<<1)//k for k in range(1,n+1))>>1) # _Chai Wah Wu_, Feb 22 2023

