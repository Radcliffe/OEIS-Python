# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A347520

# uses A053392
from collections import OrderedDict
def afiltern(terms):
    return list(OrderedDict.fromkeys(A053392(k) for k in range(terms)))
print(afiltern(179)) # _Michael S. Branicky_, Sep 04 2021

