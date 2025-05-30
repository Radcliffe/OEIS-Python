# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A063970

from sympy import divisors
def aupton(terms):
  alst = [2]
  for n in range(2, terms+1):
    alst.append(int("".join(str(d) for d in divisors(alst[-1]))))
  return alst
print(aupton(4)) # _Michael S. Branicky_, Feb 12 2021

