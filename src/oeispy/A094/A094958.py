# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A094958

def A094958(n): return 1<<n-1 if n<4 else 1<<(n>>1)+1 if n&1 else 5<<((n>>1)-2) # _Chai Wah Wu_, Feb 14 2025

