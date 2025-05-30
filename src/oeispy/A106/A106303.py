# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A106303

from itertools import count
def A106303(n):
    a = b = (0,)*4+(1 % n,)
    s = 1 % n
    for m in count(1):
        b, s = b[1:] + (s,), (s+s-b[0]) % n
        if a == b:
            return m # _Chai Wah Wu_, Feb 21-27 2022

