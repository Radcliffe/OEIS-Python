# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383739

def a(n):
    q, r = divmod(n, 5)
    if q == 0:
        return [8, 0, 2, 4, 7][r]
    if r == 0:
        return 10**q//9
    if r == 1:
        return 91*10**(q-1)//9
    return 10**(q+1)//9 + [1, 3, 6][r - 2]

