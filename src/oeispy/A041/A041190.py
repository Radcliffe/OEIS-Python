# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A041190

from sympy import sqrt
from sympy.ntheory.continued_fraction import *
def aupton(terms):
  g = continued_fraction_convergents(continued_fraction_iterator(sqrt(106)))
  return [next(g).numerator for n in range(terms)]
print(aupton(28)) # _Michael S. Branicky_, Oct 31 2021

