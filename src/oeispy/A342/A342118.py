# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342118

from fractions import Fraction
from sympy import totient
k, plist, A342118_list = 1, [Fraction(1,totient(i)) for i in range(1,7)], []
p = sum(plist)
while k < 10**7:
    if p.numerator == 1:
        A342118_list.append(k)
    k += 1
    p -= plist[0]
    plist = plist[1:] + [Fraction(1,totient(k+5))]
    p += plist[-1] # _Chai Wah Wu_, Mar 01 2021

