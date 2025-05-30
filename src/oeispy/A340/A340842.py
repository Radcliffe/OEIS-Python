# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340842

from sympy import isprime
def sd(n): return sum(map(int, str(n)))
def emirp(n):
  if not isprime(n): return False
  revn = int(str(n)[::-1])
  if n == revn: return False
  return isprime(revn)
def ok(n): return emirp(n) and emirp(n + sd(n))
def aupto(nn): return [m for m in range(1, nn+1) if ok(m)]
print(aupto(18000)) # _Michael S. Branicky_, Jan 24 2021

