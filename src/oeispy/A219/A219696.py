# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A219696

def ok(n):
    if n==1: return [1]
    N=3*n + 1
    l=[N, ]
    while True:
        if N%2==1: N = 3*N + 1
        else: N/=2
        l+=[N, ]
        if N<2: break
    if n in l: return 1
    return 0 # _Indranil Ghosh_, Apr 22 2017

