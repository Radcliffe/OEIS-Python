# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A309873

def A309873(n): return -1 if (~n & n-1).bit_length()&1 else 1 # _Chai Wah Wu_, Dec 26 2022

