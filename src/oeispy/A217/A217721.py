# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A217721

import math
def isprime(k):
  s = 3
  while s*s <= k:
    if k%s==0:  return 0
    s+=2
  return 1
for n in range(1, 333):
  c = 0
  top = n*n
  for i in range(top - int(math.log(n, 2)**2), top):
    if i&1:  c += isprime(i)
  print(str(c), end=', ')

