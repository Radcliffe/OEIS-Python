# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A033549

from sympy.ntheory.factor_ import digits
from sympy import prime
print([n for n in range(1, 1001) if sum(digits(n)[1:])==sum(digits(prime(n))[1:])]) # _Indranil Ghosh_, Jun 27 2017

