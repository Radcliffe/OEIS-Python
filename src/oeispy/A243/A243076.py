# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A243076

from sympy import prime, isprime
def a(n):
    if n==1: return 5
    p=prime(n)
    i=0
    s=0
    while i<p:
        q=(2 if i%2 else 1)*p + i
        while not isprime(q): q+=2*p
        s+=q
        i+=1
    return s
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Jun 22 2017, after Mathematica code

