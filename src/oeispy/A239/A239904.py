# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A239904

def A239904(n): return n-n.bit_count()+(n&(n>>1)).bit_count() # _Chai Wah Wu_, Feb 12 2023

