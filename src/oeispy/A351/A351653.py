# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A351653

from itertools import groupby
def A351653(n): return int(''.join(str(len(list(g))) for k, g in groupby(str(n)))) # _Chai Wah Wu_, Mar 11 2022

