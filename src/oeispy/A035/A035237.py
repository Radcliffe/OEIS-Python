# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A035237

LIMIT = 10**7
ss = set(str(i*i) for i in range(int(LIMIT**.5)+2))
def num_square_substrings(s):
  return sum(s[i:j] in ss for i in range(len(s)) for j in range(i+1, len(s)+1))
def agen():
  n, k, data = 0, 0, dict()
  while True:
    if n in data: yield data[n]; n += 1; continue
    while True:
      if k > LIMIT: assert False, "LIMIT exceeded"
      nss = num_square_substrings(str(k))
      if nss == n: data[n] = k; yield k; break
      elif nss > n:
        if nss not in data: data[nss] = k
      k += 1
    n += 1
g = agen()
for i in range(13): print(next(g)) # _Michael S. Branicky_, Dec 15 2020

