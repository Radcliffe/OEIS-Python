# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A010062

from itertools import islice
def agen():
    an = 1
    while True: yield an; an += an.bit_count()
print(list(islice(agen(), 61))) # _Michael S. Branicky_, Jul 31 2022

