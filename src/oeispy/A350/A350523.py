# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350523

from sympy import isprime
def K(n):
    ans, f = 0, 1
    for i in range(1, n+1):
        ans += f%n
        f = (f*i)%n
    return ans%n
def ok(n): return isprime(n) and (K(n) + 2)%n == 0
print([k for k in range(11000) if ok(k)]) # _Michael S. Branicky_, Jan 03 2022

