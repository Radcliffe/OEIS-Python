# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A306384

from re import split
def A306384(n):
    mset, m, c = set(), n, 0
    while True:
        if m == 1 or m == 0 or m == 5:
            return c
        m = int('0'+''.join(d for d in split('(0+)|(1+)|(2+)|(3+)|(4+)|(5+)|(6+)|(7+)|(8+)|(9+)', str(2*m)) if d != '' and d != None and len(d) == 1))
        if m in mset:
            return -1
        mset.add(m)
        c += 1

