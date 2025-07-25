# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A268083

from math import gcd
from sympy import factorint
A268083_list, b = [], 1
for n in range(1,10**4):
    if len(factorint(n)) > 1 and gcd(b,n) == 1:
        A268083_list.append(n)
    b = b*2*(2*n+1)//(n+1) # _Chai Wah Wu_, Jan 26 2016

