# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A324468

def A324468(n): return (~n & n-1).bit_length()+(~(n+1) & n).bit_length()+(~(n+2) & n+1).bit_length() # _Chai Wah Wu_, Jul 01 2022

