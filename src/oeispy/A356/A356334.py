# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356334

def A356334(n): return sum(1 for x in range((1<<n)+1) for y in range(x,(1<<n)+1) if x**(n+1)+y**(n+1)==(x+y)**n) # _Chai Wah Wu_, Sep 19 2022

