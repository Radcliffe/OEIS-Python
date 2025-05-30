# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A257342

from fractions import Fraction
from math import log10
A257342_list, m, y = [], 2, Fraction(0,1)
for i in range(2,100):
    for j in range(1,i):
        x = Fraction(j,i)
        if x.denominator == i:
            y += Fraction(int(m*x) % 2,m)
            m *= 2
for i in range(int(log10(m))-2):
    y *= 10
    A257342_list.append(int(y) % 10) # _Chai Wah Wu_, Apr 29 2015

