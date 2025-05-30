# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A323835

def A323835(n):
    mset, m, c = set(), n, 0
    while True:
        if m == 0 or m == 1:
            return c
        m = int('0'+''.join(d if str(2*m).count(d) == 1 else '' for d in str(2*m)))
        if m in mset:
            return -1
        mset.add(m)
        c += 1  # _Chai Wah Wu_, Feb 04 2019

