# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A245195

def A245195(n): return 1<<(n&(n>>1)).bit_count() # _Chai Wah Wu_, Feb 11 2023

