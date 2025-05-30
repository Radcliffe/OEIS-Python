# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A276707

# faster version skipping bad prefixes
from sympy import isprime, nextprime
def a(n):
    if n == 1: return 4
    p, c = nextprime(10**(n-1)), 0
    while p < 10**n:
        s, fail = str(p), False
        for i in range(1, n):
            ti = int(s[:i])
            if isprime(ti): fail = i; break
        if fail: p = nextprime((ti+1)*10**(n-i))
        else: p, c = nextprime(p), c+1
    return c
print([a(n) for n in range(1, 8)]) # _Michael S. Branicky_, Jul 03 2021

