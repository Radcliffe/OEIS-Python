# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342937

from itertools import groupby
def aupton(terms):
  A324608, bstr, rl_lst, rl_idx, n = [1, 1], "110", [], 0, 3
  while len(rl_lst) < terms:
    an = int(bstr[:n], 2) - int(bstr[:n-1], 2)
    binan = bin(an)[2:]
    A324608, bstr, n = A324608 + [binan.count('1')], bstr + binan, n+1
    new_runs = [len(list(g)) for k, g in groupby(A324608[rl_idx:])]
    if len(new_runs) > 0:
      rl_lst.extend(new_runs[:-1]) # don't take last one in case mid-run
      rl_idx += sum(new_runs[:-1])
  return rl_lst[:terms]
print(aupton(86)) # _Michael S. Branicky_, Mar 30 2021

