# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A108981

def A108981(n): return ((4<<(m:=n+1<<1))|2)//5-((1<<m)|2)//5>>1 # _Chai Wah Wu_, Apr 22 2025

