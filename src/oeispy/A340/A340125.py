# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340125

def ok(n):
  digs = list(map(int, str(n)))
  return sorted(digs) == digs and sum(d*(-1)**d for d in digs) == 0
def aupto(lim): return [m for m in range(lim+1) if ok(m)]
print(aupto(24455)) # _Michael S. Branicky_, Feb 21 2021

