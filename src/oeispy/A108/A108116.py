# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A108116

def SL(d, s):
  for i1 in range(int(d[0]=="0"), len(s)-int(d[0])-1):
    i2 = i1 + int(d[0]) + 1
    if not (s[i1] or s[i2]):
      s[i1] = s[i2] = d[0]
      r = d[1:]
      if r: yield from SL(r, s)
      else: yield int("".join(s))
      s[i1] = s[i2] = 0
from itertools import chain, combinations as C
def A108116gen():
  for numd in range(1, 11):
    dset, s = "0123456789", [0 for _ in range(2*numd)]
    for an in sorted(
      chain.from_iterable(SL("".join(c), s) for c in C(dset, numd))):
      yield an
for n, an in enumerate(A108116gen(), start=1):
  print(n, an) # _Michael S. Branicky_, Dec 14 2020

