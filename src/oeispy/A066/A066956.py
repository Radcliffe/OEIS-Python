# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A066956

from collections import Counter
from itertools import product, zip_longest
def aupton(nn):
    digs = list("123456789")
    c = Counter(eval("".join(filter(None, sum(zip_longest(digs, ops), ())))) for ops in product(["-", "+", ""], repeat=8))
    return [c[k] for k in range(nn+1)]
print(aupton(70)) # _Michael S. Branicky_, Nov 26 2021

