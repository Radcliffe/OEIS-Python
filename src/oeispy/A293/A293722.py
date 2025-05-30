# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A293722

def a(n):
    if n == 0: return 1
    r, l = 1, [0, 0]
    while n:
        r, l[n%2] = 2*r - l[n%2], r
        n >>= 1
    return r - 1

