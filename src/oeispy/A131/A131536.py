# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A131536

def A131536(n):
    s, t, m, k, u = '2'*n, '2'*(n+1), 0, 1, '1'
    while s not in u or t in u:
        m += 1
        k *= 2
        u = str(k)
    return m # _Chai Wah Wu_, Jan 28 2020

