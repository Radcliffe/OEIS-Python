# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352949

from sympy import isprime
print([m for m in (2*k**2+29 for k in range(140)) if not isprime(m)]) # _Michael S. Branicky_, Apr 15 2022

