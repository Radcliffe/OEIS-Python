# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A033548

from sympy.ntheory.factor_ import digits
from sympy import primepi, primerange
print([n for n in primerange(1, 5901) if (sum(digits(n)[1:])==sum(digits(primepi(n))[1:]))]) # _Indranil Ghosh_, Jun 27 2017, after _Charles R Greathouse IV_

