# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A219843

def A219843(n): return (1<<n+1)-1-sum((bool(~n&n-k)^1)<<k for k in range(n+1)) # _Chai Wah Wu_, May 03 2023

