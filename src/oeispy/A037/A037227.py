# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A037227

def A037227(n): return ((~n & n-1).bit_length()<<1)+1 # _Chai Wah Wu_, Jul 05 2022

