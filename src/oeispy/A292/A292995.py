# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A292995

from __future__ import division
def A292995(n):
    return sum(int(d) for d in str(3**n))//9 # _Chai Wah Wu_, Sep 28 2017

