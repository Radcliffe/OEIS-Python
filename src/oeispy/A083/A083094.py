# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A083094

def A083094(n): return int(bin(((m:=n-1).bit_count()&1)+(m<<1))[2:],3)<<1 # _Chai Wah Wu_, Jun 26 2025

