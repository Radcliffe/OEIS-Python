# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383218

from itertools import count
a, p = [1], 1
for k in count(2):
    if str(k) not in str(p): p *= k; a.append(p)
    if len(a) >= 20: break
print(a)

