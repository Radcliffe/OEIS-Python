# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A246136

from sympy import isprime
A246136 = []
for n in range(1,8):
    for m in range(n-1,-1,-1):
        l = ''.join([str(d) for d in range(n,m-1,-1)])
        p = int(l+l[-2::-1],8)
        if isprime(p):
            A246136.append(p)
    for m in range(n+1,8):
        l = ''.join([str(d) for d in range(n,m+1)])
        p = int(l+l[-2::-1],8)
        if isprime(p):
            A246136.append(p)
A246136 = sorted(A246136)

