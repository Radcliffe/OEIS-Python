# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A320857

from sympy import isprime; from numpy import sign
def A320857(n): return sum(isprime(i)*(i%2)*sign(i%8-4) for i in range(1,n+1)) # _Ya-Ping Lu_, Jan 25 2025

