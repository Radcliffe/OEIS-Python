# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A244060

from math import factorial
def A244060(n): return sum(int(d) for d in str(factorial(2**n))) # _Chai Wah Wu_, Oct 26 2021

