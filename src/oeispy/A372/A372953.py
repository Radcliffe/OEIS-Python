# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A372953

from itertools import count
from msmath.numfuns import primepower
def a(start=2,stop=None) :
  for n in range(start,stop) if stop else count(start):
    if primepower(n) :
      if n%4 != 3: yield n

