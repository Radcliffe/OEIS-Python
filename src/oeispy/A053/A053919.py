# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A053919

# see link in A053918 for a faster version
from math import isqrt
def aupto(limit):
  alst, rootlimit = [], isqrt(limit)
  for k in range(1, rootlimit+1):
    if set(str(k*k)) <= set("235"): alst.append(k*k)
  return alst
print(aupto(4*10**12)) # _Michael S. Branicky_, May 15 2021

