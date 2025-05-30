# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340612

def aupton(nn):
  alst, index = [0], {0: 0} # data list, map of last occurrence
  for n in range(1, nn+1):
    if n in index:
      an = index[n]
    else:
      an = alst[-1] - n
      if an < 0 or an in index:
        an = alst[-1] + n
    alst.append(an)
    index[an] = n
  return alst
print(aupton(65)) # _Michael S. Branicky_, Jan 13 2021

