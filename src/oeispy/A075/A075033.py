# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A075033

from sympy import divisor_count as tau
[n for n in range(1, 801) if tau(n) <= tau(n+1) <= tau(n+2) <= tau(n+3)] # _Karl V. Keller, Jr._, Jul 10 2020

