# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362064

from itertools import islice
def jump1(n):
    s = str(n)
    return n if "1" not in s else int(s[:(i:=s.index("1"))]+"2"+"0"*(len(s)-i-1))
def agen(): # generator of terms
    an, aset, mink = 2, {2}, 3
    while True:
        yield an
        k = mink
        while k in aset or "1" in str(an+k): k = jump1(k+1)
        an = k
        aset.add(an)
        while mink in aset: mink = jump1(mink+1)
print(list(islice(agen(), 64))) # _Michael S. Branicky_, Apr 07 2023

