# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350146

def A350146(n): return sum(k*(n//k) for k in range(1,n+1))-sum(k*(n//2//k) for k in range(1,n//2+1)) # _Chai Wah Wu_, Dec 17 2021

