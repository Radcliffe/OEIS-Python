# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A359179

from sympy import isprime
def a(n):
    c = ("".join(str(i) for i in range(1, n+1)))*2
    return sum(1 for i in range(len(c)//2) if c[i] != "0" for j in range(1, len(c)//2+1) if isprime(int(c[i:i+j])))
print([a(n) for n in range(1, 60)]) # _Michael S. Branicky_, Dec 17 2022

