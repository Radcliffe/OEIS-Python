# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A133421

from __future__ import division
def A133421(n):
    return n//2 if not n % 2 else (n//3 if not n % 3 else (n//5 if not n % 5 else 7*n+1)) # _Chai Wah Wu_, Mar 04 2018

