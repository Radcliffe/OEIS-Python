# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A087665

from fractions import Fraction
def a(n):
  b = Fraction(n, 4)
  while b.denominator != 1: b *= int(b)
  return b
for n in range(8, 15): print(a(n)) # _Michael S. Branicky_, Feb 18 2021

