# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A288185

from sympy import continued_fraction_periodic
def A288185(n):
    d = 2
    while True:
        s = continued_fraction_periodic(0,1,d)[-1]
        if isinstance(s, list) and len(s) == n:
            return d
        d += 2 # _Chai Wah Wu_, Jun 08 2017

