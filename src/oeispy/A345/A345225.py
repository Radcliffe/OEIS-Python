# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A345225

def a(n):
    n_ = (n % 8)
    d = {0:1, 1:2, 2:2, 3:16, 4:1, 5:1, 6:1}
    if n_ == 7:
        return 2*(n+1)
    else:
        return d[n_]

