# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A272636

from sympy.ntheory.factor_ import core
l=[0, 1]
for n in range(2, 101):
    l.append(core(l[n - 1] + l[n - 2]))
print(l) # _Indranil Ghosh_, Jun 03 2017

