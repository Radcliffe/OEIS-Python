# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A361743

from math import comb
def A361743(n): return sum(comb(n,k)**2*k<<k-1 for k in range(1,n+1))<<1 if n else 1 # _Chai Wah Wu_, Mar 22 2023

