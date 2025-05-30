# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342260

from sympy.ntheory.factor_ import digits
def A342260(n):
    k = 1
    while digits(k**2,n).count(n-1) != n:
        k += 1
    return k # _Chai Wah Wu_, Apr 05 2021

