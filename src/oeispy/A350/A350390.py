# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350390

from math import prod
from sympy.ntheory.factor_ import primefactors, core
def A350390(n): return n*core(n)//prod(primefactors(n)) # _Chai Wah Wu_, Dec 30 2021

