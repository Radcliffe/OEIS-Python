# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A033493

def a(n):
    if n==1: return 1
    l=[n, ]
    while True:
        if n%2==0: n//=2
        else: n = 3*n + 1
        l+=[n, ]
        if n<2: break
    return sum(l)
print([a(n) for n in range(1, 101)])  # _Indranil Ghosh_, Apr 14 2017

