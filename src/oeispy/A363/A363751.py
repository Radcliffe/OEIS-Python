# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A363751

from sympy import prime, isprime
a363751=[]
for k in range(1,101):
    if isprime(prime(k)%k):
        a363751.append(k)

