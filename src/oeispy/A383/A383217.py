# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383217

from itertools import count
from math import prod
a = [1]
while len(a) < 40: a.append(next(k for k in count(a[-1]+1) if str(k) not in str(prod(a))))
print(a)

