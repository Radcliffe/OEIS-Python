# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A234143

import math
def isTriangular(n):  # OK for relatively small n
  n+=n
  sr = int(math.sqrt(n))
  return (n==sr*(sr+1))
for n in range(1,264444):
  tn = n*(n+1)//2
  r = int(math.sqrt(tn-1))
  i = tn-r*r
  r = int(math.sqrt(tn))
  j = (r+1)*(r+1)-tn
  if isTriangular(i) and isTriangular(j):  print(str(n), end=',')

