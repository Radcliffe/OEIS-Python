# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356840

from sympy import factorint
from collections import Counter
def reversed_factors(n):
    return dict(reversed(list(factorint(n).items())))
def a(n):
    return Counter(reversed_factors(n)).most_common(1)[0][0]

