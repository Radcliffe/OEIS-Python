# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068911

def A068911(n): return 3**(n>>1)<<1 if n&1 else (3**(n-1>>1)<<2 if n else 1) # _Chai Wah Wu_, Aug 30 2024

