# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A052362

from itertools import count, islice
from num2words import num2words as n2w
def f(n): return len(n2w(n).replace(" and", "").replace(chr(44), ""))
def agen():
    record = 0
    for n in count(0):
        value = f(n)
        if value > record: yield n; record = value
print(list(islice(agen(), 46))) # _Michael S. Branicky_, Jul 12 2022

