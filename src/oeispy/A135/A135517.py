# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A135517

def A135517(n): return (1<<(~(n+1)&n).bit_length()-(not n&(n+1))) if n else 1 # _Chai Wah Wu_, Sep 18 2024

