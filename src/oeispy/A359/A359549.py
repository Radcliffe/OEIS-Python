# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A359549

from sympy import factorint
def A359549(n): return int((m:=(~n & n-1).bit_length())<2 and all(e==2 for e in factorint(n>>m).values())) # _Chai Wah Wu_, Jan 11 2023

