# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A121625

def A121625(n): return n**n*((1, 1, 0, -2)[n&3]<<((n>>1)&-2))*(-1 if n&4 else 1) # _Chai Wah Wu_, Feb 16 2024

