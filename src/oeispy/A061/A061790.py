# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A061790

def A061790(n): return (n*(n+1)>>1)-len({i**2+j**2 for i in range(1,n+1) for j in range(1,i+1)}) # _Chai Wah Wu_, Jun 27 2025

