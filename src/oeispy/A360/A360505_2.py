# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A360505

# faster version for initial segment of sequence
from sympy.ntheory import digits
from itertools import count, islice
def agen(s=""): yield from (int(s:="".join(map(str, digits(n, 3)[1:]))+s) for n in count(1))
print(list(islice(agen(), 15))) # _Michael S. Branicky_, Feb 18 2023

