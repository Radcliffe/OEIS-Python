# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A244851

def a(n):
  for k in range(1,10**5):
    st = str(3**k)
    count = 0
    if len(st) > n:
      for i in range(len(st)):
        if int(st[i]) == int(st[i+1])+1:
          count += 1
        else:
          break
      if count == n:
        return k
n = 0
while n < 10:
  print(a(n),end=', ')
  n += 1

