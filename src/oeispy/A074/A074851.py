# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A074851

import sympy
from sympy.ntheory.factor_ import primenu
for n in range(1,200):
    if primenu(n)==2 and primenu(n+1)==2:
        print(n, end=', '); # _Stefano Spezia_, Dec 05 2018

