# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A230099

from math import prod
def a(n): return n + prod(map(int, str(n)))
print([a(n) for n in range(78)]) # _Michael S. Branicky_, Jan 09 2023

