# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A061308

from __future__ import division
from sympy import prevprime, nextprime
A061308_list = [prevprime(n**3//2) for n in range(2,10**4) if prevprime(n**3//2)+nextprime(n**3//2) == n**3] # _Chai Wah Wu_, Feb 11 2018

