# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A005151

from itertools import accumulate, groupby, repeat
def summarize(n, _):
  return int("".join(str(len(list(g)))+k for k, g in groupby(sorted(str(n)))))
def aupton(nn): return list(accumulate(repeat(1, nn+1), summarize))
print(aupton(25)) # _Michael S. Branicky_, Jan 11 2021

