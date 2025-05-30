# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A333209

from math import gcd
f0, f1, g0, g1, snum, sden, n = 1, 1, 1, 2, 0, 1, 0
while n < 12:
    n = n+1
    snum, sden = g0*g1*snum+sden, sden*g0*g1
    d = gcd(snum,sden*f0)
    print(n,sden*f0//d)
    f0, f1, g0, g1 = 2*f0+f1, f0+f1, 2*g0+g1, g0+g1 # _A.H.M. Smeets_, Nov 30 2020

