# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A244415

def A244415(n): return (~n&n-1).bit_length()+1>>1 # _Chai Wah Wu_, Jul 09 2023

