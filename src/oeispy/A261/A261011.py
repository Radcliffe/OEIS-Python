# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A261011

from gmpy2 import iroot
A261011_list = [n for n in range(1,10**5) if not n % (lambda x:x[0] + (0 if x[1] else 1))(iroot(n,3))] # _Chai Wah Wu_, Aug 14 2015

