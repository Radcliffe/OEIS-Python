# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A366067

from itertools import islice
from sympy import divisor_count
def f(n): return n//dn if n%(dn:=divisor_count(n)) == 0 else n*dn
def agen(x=578): # generator of terms
    while True: yield x; x = f(x)
print(list(islice(agen(), 18))) # _Michael S. Branicky_, Oct 03 2023

