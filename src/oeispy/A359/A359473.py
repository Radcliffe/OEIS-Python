# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A359473

from sympy import factorint
def A359473(n): return int(all(map(lambda m:not((k:=m+1)&-k)^k,factorint(n).values()))) # _Chai Wah Wu_, Jan 04 2023

