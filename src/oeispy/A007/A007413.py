# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A007413

def A007413(n): return 2-(n.bit_count()&1)+((n-1).bit_count()&1) # _Chai Wah Wu_, Mar 03 2023

