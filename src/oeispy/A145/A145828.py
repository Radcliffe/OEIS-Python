# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A145828

from gmpy2 import is_square
filter(is_square, [reduce(lambda x,y:x^y, [x**2 for x in range(n)]) for n in range(1,10**4)]) # _Chai Wah Wu_, Aug 05 2014

