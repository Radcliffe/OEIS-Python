# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A069537

from itertools import product
def agen():
  digits = 1
  while True:
    for i in range(digits-2): yield int("1"+"0"*(digits-3-i)+"1"+"0"*i+"0")
    yield int("2"+"0"*(digits-1))
    digits += 1
g = agen()
print([next(g) for i in range(32)]) # _Michael S. Branicky_, Feb 20 2021

