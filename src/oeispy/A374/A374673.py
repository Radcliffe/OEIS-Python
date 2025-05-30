# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A374673

from itertools import count
from collections import Counter
from sympy import factorint
def A374673(n):
    if n==1: return 2
    c, a, l = Counter(), 0, 0
    for m in count(2):
        c += Counter(factorint(m))
        b = sum(map(int.bit_count,c.values()))
        if b==a:
            l += 1
        else:
            if l==n-1:
                return m-n
            l = 0
        a = b # _Chai Wah Wu_, Jul 18 2024

