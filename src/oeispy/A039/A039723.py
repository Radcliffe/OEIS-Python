# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A039723

def A039723(n):
    s, q = '', n
    while q >= 10 or q < 0:
        q, r = divmod(q, -10)
        if r < 0:
            q += 1
            r += 10
        s += str(r)
    return int(str(q)+s[::-1]) # _Chai Wah Wu_, Apr 10 2016

