# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A063224

def A063224(n): return n-1+sum(divmod(n-1,3)) # _Chai Wah Wu_, Jan 29 2023

