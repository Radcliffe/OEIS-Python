# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354463

from sympy import factorial, multiplicity
def a(n): return multiplicity(5, factorial(2**n, evaluate=False))
print([a(n) for n in range(39)]) # _Michael S. Branicky_, Jun 01 2022

