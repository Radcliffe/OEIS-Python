# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A380024

def A380024(n): return (1<<(n<<1))-((n*(n-1)>>1)+9)*3**(n-2) if n>1 else n # _Chai Wah Wu_, Feb 14 2025

