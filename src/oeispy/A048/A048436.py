# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A048436

from functools import reduce
def A048436(n): return reduce(lambda i,j:(i<<(bool((m:=j.bit_length())&1)<<1)+(m&-2))+j,range(n+1)) # _Chai Wah Wu_, Feb 26 2023

