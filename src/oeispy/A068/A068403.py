# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068403

from sympy import divisor_sigma
print([n for n in range(180, 3001) if divisor_sigma(n)>3*n]) # _Indranil Ghosh_, Apr 10 2017

