# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A317295

from sympy import isprime; isok = lambda n: n & (n-1) and not isprime(bin(n).count('1')) # _David Radcliffe_, Aug 15 2018

