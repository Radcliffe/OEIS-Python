# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A215581

TOP = 1000
a = [0]*TOP
a[1] = 1
n = 2
k = 1
while n+k*2 < TOP:
  a[n:] = a[n-k:n]
  n += k
  a[n:] = a[:k]
  n += k
  k += 1
for k in range(n):
  print(a[k], end=', ')

