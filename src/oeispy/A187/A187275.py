# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A187275

def A187275(n): return n*5**(1+(n>>1)) if n&1 else 3*n*5**(n>>1) # _Chai Wah Wu_, Feb 19 2024

