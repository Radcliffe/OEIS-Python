# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A083652

def A083652(n): return 2+(n+1)*(m:=(n+1).bit_length())-(1<<m) # _Chai Wah Wu_, Mar 01 2023

