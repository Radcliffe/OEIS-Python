# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A137079

from itertools import product
A137079_list = [int(''.join(a)+b) for l in range(10) for a in product('2356',repeat = l) for b in ('5','6') if set(str(int(''.join(a)+b)**2)) <= {'2','3','5','6'}]
# _Chai Wah Wu_, Apr 29 2015

