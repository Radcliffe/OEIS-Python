# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A289815

from sympy import gcd, primefactors
def omega(n): return 0 if n==1 else len(primefactors(n))
def a(n):
    v, x, o = 1, 1, 2
    while True:
        if n==0: return v
        if gcd(x, o)==1 and omega(o)==1:
            if n%3: x*=o
            if n%3==1:v*=o
            n //= 3
        o+=1
print([a(n) for n in range(101)]) # _Indranil Ghosh_, Aug 02 2017

