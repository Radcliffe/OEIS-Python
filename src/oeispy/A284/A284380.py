# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A284380

from sympy.utilities.iterables import multiset_permutations
def aupton(terms):
  n, digits, alst = 0, 1, []
  while len(alst) < terms:
    mpstr = "".join(d*digits for d in "57")
    for mp in multiset_permutations(mpstr, digits):
      alst.append(int("".join(mp)))
      if len(alst) == terms: break
    else: digits += 1
  return alst
print(aupton(44)) # _Michael S. Branicky_, May 07 2021

