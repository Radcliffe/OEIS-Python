# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A369395

from math import factorial
def A369395(n): return n**n*((n+1)**n-(factorial(n)<<n))  # _Chai Wah Wu_, Jan 25 2024

