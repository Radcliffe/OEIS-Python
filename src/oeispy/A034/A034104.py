# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A034104

from math import sqrt
def ok(n): r = sqrt(n); return int(10*(r-int(r))) == 8
print(list(filter(ok, range(524)))) # _Michael S. Branicky_, Aug 15 2021

