# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A318725

from itertools import count
from sympy.ntheory import digits
def A318725(n):
    c, flag = 1, False
    for k in count(1):
        m = k
        if flag:
            a, b = divmod(m,n)
            while not b:
                m = a
                a, b = divmod(m,n)
        c *= m
        if len(set(digits(c,n)[1:]))==n:
            return k
        if not (flag or c%n):
            flag = True # _Chai Wah Wu_, Mar 13 2024

