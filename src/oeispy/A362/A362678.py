# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362678

from sympy import isprime
from itertools import count, combinations_with_replacement as cwr, islice
def agen(): yield from (filter(isprime, (int("".join(c)) for d in count(1) for c in cwr("2357",d))))
print(list(islice(agen(), 50))) # _Michael S. Branicky_, Jul 05 2023

