# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A252043

from itertools import islice
def bgen(): yield from (c for n in count(1) for c in str(n) )
def agen():
    s, g = "", bgen()
    while True:
        s += next(g); yield int(s)
print(list(islice(agen(), 20))) # _Michael S. Branicky_, Oct 25 2022

