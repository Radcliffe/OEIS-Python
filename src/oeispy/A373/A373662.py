# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A373662

def A373662(n): return ((n+1)*(n+2)-1 if n&1 else n*(n+1)+5)>>1 # _Chai Wah Wu_, Jun 23 2024

