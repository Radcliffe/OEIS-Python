# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A225218

from itertools import count, islice
def c(n): return len(set(str(n))) == 10
def agen(): yield from (k*k for k in count(31622) if c(k*k))
print(list(islice(agen(), 21))) # _Michael S. Branicky_, Dec 27 2022

