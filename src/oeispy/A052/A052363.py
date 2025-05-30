# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A052363

from itertools import count, islice
from num2words import num2words as n2w
def f(n): return sum(1 for c in n2w(n).replace(" and", "") if c.isalpha())
def agen():
    record = 0
    for n in count(0):
        value = f(n)
        if value > record: yield n; record = value
        n += 1
print(list(islice(agen(), 40))) # _Michael S. Branicky_, Jul 12 2022

