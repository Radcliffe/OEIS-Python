# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A266235

from sympy import isprime
a=[]
TOP=1000000
for p in range(TOP):
    if isprime(p):
        q=p
        while q<TOP:
            q = q*q+1
            if isprime(q):
                a.append(q)
print(sorted(set(a)))

