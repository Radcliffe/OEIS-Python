# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A061357

from sympy import primerange, isprime
def A061357(n): return sum(1 for p in primerange(n) if isprime((n<<1)-p)) # _Chai Wah Wu_, Sep 03 2024

