# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A006582

def A006582(n): return sum(k^n-k for k in range(1,n+1>>1))<<1 # _Chai Wah Wu_, May 07 2023

