# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A247178

from sympy import nextprime, isprime
p=2
s=0
while 0 < p < 10000:
    np=nextprime(p)
    if isprime(s):
        print(p)
    d=np-p
    s+=(d*d*d)
    p=np

