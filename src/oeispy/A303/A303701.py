# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A303701

from num2words import num2words
def n2w(n):
  map = {ord(c): None for c in "-, "}
  return num2words(n).replace(" and", "").translate(map)
def a(n): return len(set(n2w(n)))
print([a(n) for n in range(98)]) # _Michael S. Branicky_, Apr 03 2021

