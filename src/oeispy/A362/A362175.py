# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362175

from itertools import count
def a(n): return next(k for k in count(2) if (s:=str(k)).strip("0")!="1" and str(k**n).startswith(s))
print([a(n) for n in range(3, 75)]) # _Michael S. Branicky_, Apr 11 2023

