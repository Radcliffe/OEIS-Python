# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A060958

from dateutil.easter import *
def a(n): return (easter(n).month-3)*31 + easter(n).day
print([a(n) for n in range(2001, 2067)]) # _Michael S. Branicky_, Apr 04 2021

