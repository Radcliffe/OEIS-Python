# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352808

from itertools import count, islice
def agen(): # generator of terms
    alst = [0, 1]; aset = {0, 1}; yield from alst
    mink = 2
    for n in count(2):
        ahalf, k = alst[n//2], mink
        while k in aset or k&ahalf: k += 1
        alst.append(k); aset.add(k); yield k
        while mink in aset: mink += 1
print(list(islice(agen(), 67))) # _Michael S. Branicky_, May 17 2022

