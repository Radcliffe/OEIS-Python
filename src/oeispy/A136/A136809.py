# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A136809

from itertools import count, islice
def agen(only="0123"):
    digset, valid = set(only), set(only)
    for e in count(1):
        found, newvalid = set(), set()
        for tstr in valid:
            t = int(tstr)
            if (tstr == "0" or tstr[0] != "0") and set(str(t**2)) <= digset:
                found.add(t)
            for d in digset:
                dtstr = d + tstr
                dt = int(dtstr)
                remstr = str(dt**2)[-e:]
                if set(remstr) <= digset:
                    newvalid.add(dtstr)
        valid = newvalid
        yield from sorted(found)
print(list(islice(agen(), 50))) # _Michael S. Branicky_, Jul 07 2022

