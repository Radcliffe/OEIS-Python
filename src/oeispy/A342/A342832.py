# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342832

def aupto(limit):
  ofps = [i**4 for i in range(1, int(limit**.25)+2, 2) if i**4 < limit]
  ss = set(f+g for i, f in enumerate(ofps) for g in ofps[i+1:])
  return sorted(s for s in ss if s <= limit)
print(aupto(132722)) # _Michael S. Branicky_, Apr 24 2021

