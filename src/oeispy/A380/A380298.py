# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A380298

from itertools import count, islice
def agen(): # generator of terms
    adict, an, m, s, sn = dict(), 1, 1, "", [None]
    for n in count(1):
        yield an
        s += str(an)
        sn.append(len(s))
        adict[an] = [n] if an not in adict else adict[an] + [n]
        an = next(k for k in count(m) if k not in adict or (len(adict[k])==1 and str(k) in s[sn[adict[k][0]]:]))
        while m in adict and len(adict[m]) > 1: m += 1
print(list(islice(agen(), 70))) # _Michael S. Branicky_, Jan 19 2025

