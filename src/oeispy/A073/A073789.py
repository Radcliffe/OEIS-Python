# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A073789

def A073789(n):
    s, q = '', n
    while q >= 8 or q < 0:
        q, r = divmod(q, -8)
        if r < 0:
            q += 1
            r += 8
        s += str(r)
    return int(str(q)+s[::-1]) # _Chai Wah Wu_, Apr 09 2016

