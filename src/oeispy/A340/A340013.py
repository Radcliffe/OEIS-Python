# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340013

from sympy import factorial, nextprime, prevprime
def A340013(n):
    f = factorial(n)
    return (nextprime(f)-prevprime(f))//2 # _Chai Wah Wu_, Jan 23 2021

