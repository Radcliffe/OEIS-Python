# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342949

from math import prod
def pd(o): return prod(int(d) for d in str(o))
def aupto(limit):
  return [o for o in range(1, limit+1, 2) if pd(o) and o%pd(o) == 0]
print(aupto(111135)) # _Michael S. Branicky_, Mar 30 2021

