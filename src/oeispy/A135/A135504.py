# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A135504

from sympy import lcm
l=[0, 1]
for n in range(2, 101):
    x=l[n - 1]
    l.append(x + lcm(x, n))
print(l) # _Indranil Ghosh_, Jun 27 2017

