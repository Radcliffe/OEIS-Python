# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A341008

def ok(n):
  s = str(n)
  return abs(sum(map(int, s))-2*sum(int(d) for d in s if d in "2468")) == 7
print(list(filter(ok, range(900)))) # _Michael S. Branicky_, Jul 18 2021

