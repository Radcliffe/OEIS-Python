# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348667

for n in range(1060):
  i = x = 1
  while x:
    x = (x+i) % (n+i)
    i += 1
  print(i, end=', ')

