# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A187751

import math
for n in range(12):
  f = math.factorial(n)
  print(pow(n, f, f**n))

