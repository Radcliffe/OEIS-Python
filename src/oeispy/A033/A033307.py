# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A033307

from itertools import count
def agen():
    for k in count(1): yield from list(map(int, str(k)))
a = agen()
print([next(a) for i in range(104)]) # _Michael S. Branicky_, Sep 13 2021

