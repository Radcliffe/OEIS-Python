# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A368366

from math import factorial
def A368366(n): return ((m:=n**n)*(n+1)**n>>n)-m*factorial(n) # _Chai Wah Wu_, Jan 25 2024

