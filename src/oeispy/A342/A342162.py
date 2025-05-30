# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342162

from itertools import count
def A342162(n):
    s1, s2, m = tuple(int(d) for d in str(n)), tuple(), -1
    l = len(s1)
    for i, s in enumerate(int(d) for k in count(0) for d in str(k)):
        s2 = (s2+(s,))[-l:]
        if s2 == s1:
            if m >= 0:
                return i-m
            m = i # _Chai Wah Wu_, Feb 18 2022

