# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A061910

from gmpy2 import is_square
A061910 = [n for n in range(1,10**3) if is_square(sum(int(d) for d in str(n*n)))] # _Chai Wah Wu_, Sep 03 2014

