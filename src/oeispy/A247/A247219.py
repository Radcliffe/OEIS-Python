# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A247219

from gmpy2 import powmod
A247219_list = [n for n in range(2,10**7) if powmod(2,n,n*n-1) == 1]
# _Chai Wah Wu_, Dec 03 2014

