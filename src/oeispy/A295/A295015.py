# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A295015

from math import isqrt
def aupto(limit):
  alst, rootlimit = [], isqrt(limit)
  for k in range(1, rootlimit+1):
    if max(str(k*k)) == "5": alst.append(k*k)
  return alst
print(aupto(302500)) # _Michael S. Branicky_, May 15 2021

