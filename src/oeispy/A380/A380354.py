# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A380354

from functools import reduce
from sympy import totient, primerange
def A380354(n): return totient(reduce(lambda x,y:totient(x)+y,tuple(reversed(tuple(primerange(prime(n)+1)))))) # _Chai Wah Wu_, Jan 23 2025

