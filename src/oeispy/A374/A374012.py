# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A374012

from itertools import count
from sympy.solvers.diophantine.diophantine import power_representation
def A374012(n):
    if n == 1: return 1
    for k in count(1):
        try:
            next(power_representation(n,6,k))
        except:
            continue
        return k # _Chai Wah Wu_, Jun 25 2024

