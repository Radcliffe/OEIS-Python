# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A343951

def ok(n):
  d, sums = str(n), set()
  for i in range(len(d)):
    for j in range(i, len(d)):
      sij = sum(map(int, d[i:j+1]))
      if sij in sums: return False
      else: sums.add(sij)
  return True
print(list(filter(ok, range(83)))) # _Michael S. Branicky_, May 05 2021

