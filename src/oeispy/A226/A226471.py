# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A226471

import math
for n in range(100000000):
  a = (n*n) ^ (n*(n+1)//2)
  r = int(math.sqrt(a*2))
  if r*(r+1)==a*2: print(n, end=', ')

