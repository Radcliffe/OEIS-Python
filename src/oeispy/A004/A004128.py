# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A004128

def A007949(n):
    c = 0
    while not (a:=divmod(n,3))[1]:
        c += 1
        n = a[0]
    return c
def A004128(n): return n+sum(A007949(i) for i in range(3,n+1)) # _Chai Wah Wu_, Feb 28 2025

