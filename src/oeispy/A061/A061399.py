# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A061399

from sympy import mobius, prime
def A061399(n): return sum(not mobius(m) for m in range(prime(n)+1,prime(n+1))) # _Chai Wah Wu_, Jul 20 2024

