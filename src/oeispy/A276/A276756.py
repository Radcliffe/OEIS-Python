# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A276756

from fractions import Fraction
from sympy import factorint, primefactors
A276756_list = [1] + [n for n in range(2,10**6) if max(factorint(n).values()) <= 1 and sum(Fraction(p,10**len(str(p))) for p in primefactors(n)).denominator == 1]

