# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356133

def A356133(n): return 3*n-(2 if (n-1).bit_count()&1 else 1) # _Chai Wah Wu_, Mar 01 2023

