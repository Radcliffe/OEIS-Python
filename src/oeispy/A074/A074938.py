# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A074938

def A074938(n): return int(bin((n<<1)+(n.bit_count()&1^1))[2:],3) # _Chai Wah Wu_, Jun 26 2025

