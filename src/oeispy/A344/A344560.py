# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A344560

from sympy import hyperexpand, Rational
from sympy.functions import hyper
def A344560(n): return hyperexpand(hyper((Rational(-n,3),Rational(1-n,3),Rational(2-n,3)),(1,1),-27)) # _Chai Wah Wu_, Jan 04 2024

