# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A351412

def A351412(n):
    if n == 1:
        return 1
    q, r = divmod(n, 4)
    if r == 0:
        return n-q+1
    elif r == 2:
        return n-q
    elif r == 1:
        return n+2*q-1
    else:
        return n+2*q # _Chai Wah Wu_, Feb 19 2022

