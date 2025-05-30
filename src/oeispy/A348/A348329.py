# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348329

from sympy import factorint
from itertools import count, islice
def ad(n): return 0 if n<2 else sum(n*e//p for p, e in factorint(n).items())
def agen(): yield from (k for k in count(0) if (adk:=ad(k)) == ad(adk))
print(list(islice(agen(), 5))) # _Michael S. Branicky_, Oct 12 2022

