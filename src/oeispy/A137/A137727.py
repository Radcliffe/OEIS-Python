# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A137727

from sympy import prime
def a(n): return (prime(n)*prime(n+1))%10
print([a(n) for n in range(1, 106)]) # _Michael S. Branicky_, Jun 05 2021

