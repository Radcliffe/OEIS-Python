# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A020985

def A020985(n): return -1 if (n&(n>>1)).bit_count()&1 else 1 # _Chai Wah Wu_, Feb 11 2023

