# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A318053

import math
r = []
r.append(1)
r.append(1)
i = 2
while i < 1001:
  r.append(math.ceil(math.sqrt(2*r[i-1]*r[i-2])))
  i += 1
print(r)

