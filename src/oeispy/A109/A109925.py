# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A109925

from sympy import isprime
def A109925(n): return sum(1 for i in range(n.bit_length()) if isprime(n-(1<<i))) # _Chai Wah Wu_, Nov 29 2023

