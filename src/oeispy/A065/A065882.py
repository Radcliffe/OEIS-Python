# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A065882

def A065882(n): return (n>>((~n & n-1).bit_length()&-2))&3 # _Chai Wah Wu_, Aug 21 2023

