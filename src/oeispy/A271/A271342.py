# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A271342

def A271342(n): return sum(k*((n>>1)//k) for k in range(1, (n>>1)+1))<<1 # _Chai Wah Wu_, Apr 26 2023

