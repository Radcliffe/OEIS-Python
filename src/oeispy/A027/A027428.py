# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A027428

def A027428(n): return len({i*j for i in range(1,n+1) for j in range(1,i)}) # _Chai Wah Wu_, Oct 13 2023

