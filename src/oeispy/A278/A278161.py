# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A278161

def A278161(n): return sum(int(not (~(n+3*k) & 6*k) | (~n & k)) for k in range(n+1)) # _Chai Wah Wu_, Sep 28 2021

