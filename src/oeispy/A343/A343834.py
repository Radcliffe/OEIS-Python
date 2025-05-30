# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A343834

from sympy import isprime
from sympy.utilities.iterables import multiset_combinations
def aupton(terms):
  n, digits, alst = 0, 1, []
  while len(alst) < terms:
    mcstr = "".join(d*digits for d in "2357")
    for mc in multiset_combinations(mcstr, digits):
      sd = sum(int(d) for d in mc)
      if not isprime(sd): continue
      t = int("".join(mc))
      if isprime(t): alst.append(t)
      if len(alst) == terms: break
    else: digits += 1
  return alst
print(aupton(35)) # _Michael S. Branicky_, May 01 2021

