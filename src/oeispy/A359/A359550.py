# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A359550

from sympy import factorint
def A359550(n): return int(all(map(lambda d:d[0]>d[1],factorint(n).items()))) # _Chai Wah Wu_, Jan 06 2023

