# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A091157

from sympy import isprime, fibonacci as F, lucas as L
print([3]+list(filter(isprime, (F(k)+L(k+1) for k in range(1, 101)))))
# _Michael S. Branicky_, Jul 31 2022

