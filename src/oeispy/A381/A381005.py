# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A381005

def A381005(n): return ((m:=1<<(n<<1)-1)-1)*(3*m+1) # _Chai Wah Wu_, Feb 13 2025

