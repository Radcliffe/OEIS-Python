# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A106481

# uses programs from A002088 and A049690
def A106481(n): return A002088(n+1)-A049690(n+1>>1) if n&1 else A049690(n>>1) # _Chai Wah Wu_, Aug 04 2024

