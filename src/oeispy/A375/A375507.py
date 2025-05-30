# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375507

from itertools import count
def A375507_list(nmax):
    a = [1]
    def digits():
        for i in count():
            for d in str(a[i]):
                yield int(d)
    diff = 0
    for n,d in enumerate(digits(),1):
        if n==nmax: return a
        diff = 10*diff+d
        a.append(a[-1]+diff) # _Pontus von Brömssen_, Aug 18 2024

