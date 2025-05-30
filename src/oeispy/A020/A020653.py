# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A020653

from sympy import totient, gcd
def a(n):
    s=0
    k=2
    while s<n:
        s+=totient(k)
        k+=1
    s-=totient(k - 1)
    j=1
    while s<n:
        if gcd(j, k - 1)==1: s+=1
        j+=1
    return k - j # _Indranil Ghosh_, May 23 2017, translated from Ulrich Schimke's MAPLE code

