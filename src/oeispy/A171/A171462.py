# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A171462

from sympy import primefactors
def a(n): return 0 if n == 1 else n - n//(primefactors(n)[-1])
print([a(n) for n in range(1, 74)]) # _Michael S. Branicky_, Apr 19 2021

