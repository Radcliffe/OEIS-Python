# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A245340

from itertools import count
def A245340(n):
    a, aset = 0, set()
    for m in count(1):
        if a==n: return m-1
        aset.add(a)
        a = next(a for a in count(a%m,m) if a not in aset) # _Chai Wah Wu_, Mar 13 2024

