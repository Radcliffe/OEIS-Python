# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A161400

from itertools import product
def bin_pals():
  yield "1"
  digits, midrange = 2, [[""], ["0", "1"]]
  while True:
    for p in product("01", repeat=digits//2-1):
      left = "1"+"".join(p)
      for middle in midrange[digits%2]:
        yield left+middle+left[::-1]
    digits += 1
def aupton(terms):
  alst, bgen = [], bin_pals()
  while len(alst) < terms: b = next(bgen); alst.append(int(b+b, 2))
  return alst
print(aupton(37)) # _Michael S. Branicky_, Mar 15 2021

