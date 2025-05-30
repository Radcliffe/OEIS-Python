# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A345906

from sympy import isprime
def ok(n):
    if n <= 1000: return False
    s = str(n)
    return all(isprime(int(s[i:i+3])) for i in range(len(s)-2))
print(list(filter(ok, range(1001, 2300)))) # _Michael S. Branicky_, Jun 29 2021

