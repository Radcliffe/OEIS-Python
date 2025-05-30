# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342871

from sympy import integer_nthroot
def A342871(n):
    c = 0
    for k in range(1,n+1):
        m = integer_nthroot(n,k)[0]
        if m == 1:
            return c+n-k+1
        else:
            c += m
    return c # _Chai Wah Wu_, Apr 06 2021

