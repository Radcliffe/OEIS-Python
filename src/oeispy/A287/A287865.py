# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A287865

from sympy import primefactors
l=[0, 1]
for n in range(2, 77):
    l.append(primefactors(2*l[n - 1] + 1)[-1])
print(l[1:]) # _Indranil Ghosh_, Jun 04 2017

