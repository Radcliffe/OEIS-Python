# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A180278

from itertools import count
from sympy import factorint
def A180278(n):
    return next(k for k in count() if len(factorint(k**2+1)) == n) # _Pontus von Brömssen_, Sep 12 2023

