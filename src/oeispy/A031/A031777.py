# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A031777

from sympy import continued_fraction_periodic
A031777_list = [n for n, d in ((n, continued_fraction_periodic(0,1,n)[-1]) for n in range(1,10**5)) if isinstance(d, list) and min(d) == 99] # _Chai Wah Wu_, Jun 10 2017

