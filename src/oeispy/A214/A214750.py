# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A214750

from sympy.abc import x, y
from sympy.solvers.diophantine.diophantine import diop_quadratic
def A214750(n): return min(int(x) for x,y in diop_quadratic(n*(n-y)+x*(y+x)) if x>0) # _Chai Wah Wu_, Oct 06 2023

