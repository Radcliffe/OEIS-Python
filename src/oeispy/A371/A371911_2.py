# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371911

# faster for initial segment of sequence
from itertools import islice
def agen(): # generator of terms
    a, b, c = 1, 1, 1
    while True: yield a; a, b, c = b, c, int(str(a+b+c).replace("0", ""))
print(list(islice(agen(), 50))) # _Michael S. Branicky_, Apr 13 2024

