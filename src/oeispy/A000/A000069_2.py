# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A000069

def A000069(n): return ((m:=n-1)<<1)+(m.bit_count()&1^1) # _Chai Wah Wu_, Mar 03 2023

