# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A373299

from sympy import prime
def ok(k):
    return prime(k)-prime(k-1) == prime(k+2)-prime(k+1)
print([prime(k) for k in range(2,200) if ok(k)])

