# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A070198

from math import lcm
def A070198(n): return lcm(*range(1,n+2))-1 # _Chai Wah Wu_, May 02 2023

