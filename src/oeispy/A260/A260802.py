# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A260802

import sympy
n=1
while n>0:
    s=str(n)
    for m in range(n-2,0,-2):
        s=str(m)+s+str(m)
    p=int(s)
    if sympy.isprime(p)==True:
        print(n)
    n=n+2

