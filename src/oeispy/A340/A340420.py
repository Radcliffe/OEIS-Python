# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340420

from sympy import isprime
for n in range(1, 101):
    ct, m = 0, n
    while m > 1:
        if m%2 == 0: m //= 2
        elif isprime(m) == 1: m = 3*m + 1
        else: m -= 1
        ct += 1
    print(ct)

