# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A281316

from sympy import isprime
def G(n):
    return int(bin(n^(n//2))[2:], 2)
i=1
j=1
while j<=10000:
    if  isprime(i)==True and isprime(G(i))==True:
        print(f"{j} {i}")
        j+=1
    i+=1

