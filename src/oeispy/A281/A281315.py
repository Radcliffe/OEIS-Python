# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A281315

from sympy import isprime
def t(n):
    s=0
    for a in range(n+1):
        for d in range(n+1):
            ad = a * d
            for c in range(n+1):
                for b in range(n+1):
                    if isprime(ad-b*c):
                        s+=1
    return s
for i in range(187):
    print(str(i)+" "+str(t(i)))

