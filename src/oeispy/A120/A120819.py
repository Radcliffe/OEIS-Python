# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A120819

from sympy import isprime
L = ['8901', '234567']; s = '1234567'; c = len(s); m = 0
while c < 18881:
    s += L[m%2]; c = len(s); m += 1
    if isprime(int(s)): print(c, end = ', ')  # _Ya-Ping Lu_, Jan 24 2025

