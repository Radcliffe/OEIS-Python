# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356754

# Indexed as a linear sequence.
def a000124(n): return n*(n+1)//2 + 1
def a(n):
    l = m = 0
    for k in range(1,n):
        lc = a000124(k - 1)
        if n >= lc:
            l = lc
            m = k
        else: break
    return n + m + (n - l)

