# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A178465

def A178465(n): return n+(m:=n&1)+(n*(n**2-m)>>1) if n != 1 else 0 # _Chai Wah Wu_, Aug 30 2022

