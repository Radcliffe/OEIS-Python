# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A318510

from math import prod
from functools import reduce
from sympy import factorint, nextprime
def A318510(n): return prod(sum(reduce(lambda x,y:(x[0],x[0]+x[1]) if int(y) else (x[0]+x[1],x[1]),bin(nextprime(p))[-1:2:-1],(1,0)))**e for p, e in factorint(n).items()) # _Chai Wah Wu_, May 18 2023

