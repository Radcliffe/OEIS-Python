# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A097383

def A097383(n): return (n+1)*(m:=n.bit_length())-(1<<m)-(n-1>>1) # _Chai Wah Wu_, Mar 29 2023

