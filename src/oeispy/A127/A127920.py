# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A127920

from sympy import prime
print([(prime(n) - 1)*prime(n)*(prime(n) + 1)//6 for n in range(1, 101)]) # _Indranil Ghosh_, Apr 09 2017

