# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A300000

def a(n):
    alist, c, ckm1 = [1, 10], "110", 11
    for k in range(3, n+1):
        ck = 10*ckm1 + int(c[k-1])
        ak, ckm1 = ck - ckm1, ck
        c += str(ak)
        alist.append(ak)
    return alist[n-1]
print([a(n) for n in range(1, 24)]) # _Michael S. Branicky_, Dec 07 2020

