# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A051270

from sympy import primefactors
print([n for n in range(2, 20001) if len(primefactors(n))==5]) # _Indranil Ghosh_, Apr 06 2017

