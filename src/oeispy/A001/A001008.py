# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A001008

from sympy import Integer
[sum(1/Integer(i) for i in range(1, n + 1)).numerator() for n in range(1, 31)]  # _Indranil Ghosh_, Mar 23 2017

