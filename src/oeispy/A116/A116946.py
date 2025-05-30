# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A116946

from sympy import factorint
def semiprime(n): return sum(e for e in factorint(n).values()) == 2
def nextsemiprime(n):
  nxt = n + 1
  while not semiprime(nxt): nxt += 1
  return nxt
def aupton(terms):
  prv, cur, nxt, alst = 0, 4, 6, []
  while len(alst) < terms:
    alst.append(prv if 2*cur - prv <= nxt else nxt)
    prv, cur, nxt = cur, nxt, nextsemiprime(nxt)
  return alst
print(aupton(59)) # _Michael S. Branicky_, Jun 04 2021

