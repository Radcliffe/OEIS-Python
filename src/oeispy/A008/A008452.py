# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A008452

# uses Python code from A000143
from math import isqrt
def A008452(n): return A000143(n)+(sum(A000143(n-k**2) for k in range(1,isqrt(n)+1))<<1) # _Chai Wah Wu_, Jun 23 2024

