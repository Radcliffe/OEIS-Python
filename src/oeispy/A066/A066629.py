# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A066629

from sympy import fibonacci
def A066629(n): return (fibonacci(n+2)<<1)-1-(n&1) # _Chai Wah Wu_, May 05 2025

