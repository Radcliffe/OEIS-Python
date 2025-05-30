# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A212529

def A212529(n):
    s, q = '', -n
    while q >= 2 or q < 0:
        q, r = divmod(q, -2)
        if r < 0:
            q += 1
            r += 2
        s += str(r)
    return int(str(q)+s[::-1]) # _Chai Wah Wu_, Apr 09 2016

