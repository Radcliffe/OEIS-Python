# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377444

from itertools import count
from sympy.solvers.diophantine.diophantine import power_representation
def A377444(n): return next(filter(lambda k:len(list(power_representation(k**3,3,3)))==n,count(1))) # _Chai Wah Wu_, Nov 19 2024

