# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A057683

from sympy import isprime
A057683_list = [n for n in range(10**5) if isprime(n**2+n+1) and isprime(n**3+n+1) and isprime(n**4+n+1)] # _Chai Wah Wu_, Apr 02 2021

