# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068773

# uses code from A002088 and A049690
def A068773(n): return A002088(n)-(A049690(n>>1)<<1) # _Chai Wah Wu_, Aug 04 2024

