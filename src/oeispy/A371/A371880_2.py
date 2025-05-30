# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371880

from itertools import islice
def reverse(n): return int(str(n)[::-1])
def agen(): # generator of terms
    reach = {1}
    while True:
        yield min(reach)
        newreach = set()
        for q in reach: newreach.update([2*q, reverse(2*q)])
        reach = newreach
print(list(islice(agen(), 28))) # _Michael S. Branicky_, Apr 14 2024

