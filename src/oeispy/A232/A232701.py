# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A232701

import math
o=1
for n in range(1,99,2):
  o*=n
  print(o % math.factorial(n//2+1), end=', ')

