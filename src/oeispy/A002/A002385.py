# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A002385

from itertools import chain
from sympy import isprime
A002385 = sorted((n for n in chain((int(str(x)+str(x)[::-1]) for x in range(1,10**5)),(int(str(x)+str(x)[-2::-1]) for x in range(1,10**5))) if isprime(n))) # _Chai Wah Wu_, Aug 16 2014

