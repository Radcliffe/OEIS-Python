# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370259

from sympy import chebyshevt
def A370259(n): return (chebyshevt(n,n+1)-1)//n**3 # _Chai Wah Wu_, Mar 13 2024

