# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A116018

from sympy import totient
A116018 = [n for n in range(1,10**6) if len(set(str(n+totient(n)))) == 1] # _Chai Wah Wu_, Aug 11 2014

