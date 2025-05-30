# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A344936

from sympy import isprime, nextprime
def insert_zeros(n, k): return int(("0"*k).join(list(str(n))))
def ok(p, n): return all(isprime(insert_zeros(p, k)) for k in range(1, n+1))
def a(n, startat=11):
  p = startat
  while True:
    if ok(p, n): return p
    p = nextprime(p)
print([a(n) for n in range(1, 6)]) # _Michael S. Branicky_, Jun 03 2021

