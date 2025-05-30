# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357377

from itertools import count, islice
def agen(): # generator of terms
    alst, aset, astr, an, mink, mindiff = [], set(), "", 0, 1, 1
    for n in count(0):
        yield an; aset.add(an); astr += str(an)
        prevan, an = an, mink
        while an + mindiff <= prevan and (an in aset or str(abs(an-prevan)) in astr): an += 1
        if an in aset or str(abs(an-prevan)) in astr:
            an = max(mink, prevan + mindiff)
            while an in aset or str(an-prevan) in astr:
                an += 1
        while mink in aset: mink += 1
        while str(mindiff) in astr: mindiff += 1
print(list(islice(agen(), 75))) # _Michael S. Branicky_, Oct 05 2022

