# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A329722

def A329722(n): return sum(int(not (~(n+2*k) & 2*n-k) | (~n & k)) for k in range(n+1)) # _Chai Wah Wu_, Sep 28 2021

