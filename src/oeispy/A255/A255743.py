# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A255743

# Python 3.10+
def A255743(n): return 1 if n == 1 else 9*(1<<((n-1).bit_count()-1)*3) # _Chai Wah Wu_, Nov 15 2022

