# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A036059

def aupton(nn):
  alst = [1, 1]
  for n in range(2, nn+1):
    prev2, anstr = sorted(str(alst[-2]) + str(alst[-1])), ""
    for d in sorted(set(prev2), reverse=True):
      anstr += str(prev2.count(d)) + d
    alst.append(int(anstr))
  return alst
print(aupton(20)) # _Michael S. Branicky_, Feb 02 2021

