# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355222

from itertools import accumulate
def A355222(n): return int(''.join(accumulate(str(n),func=max))) # _Chai Wah Wu_, Jun 25 2022

