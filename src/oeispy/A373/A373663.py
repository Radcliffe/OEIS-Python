# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A373663

def A373663(n): return ((n+1)*(n+2)+6 if n&1 else (n+2)*(n+3)-4)>>1 # _Chai Wah Wu_, Jun 23 2024

