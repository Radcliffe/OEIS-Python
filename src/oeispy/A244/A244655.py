# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A244655

def a(n):
  for k in range(1, 10**9):
    st = str(3**k)
    if len(st) > n:
      count = 0
      for i in range(len(st)):
        if int(st[len(st)-1-i]) == int(st[len(st)-2-i])-1:
          count += 1
        else:
          break
      if count == n:
        return k
n = 0
while n < 10:
  print(a(n), end=', ')
  n += 1

