# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A232821

def sub(n):
  num = n**(n-1)
  for i in range(0, n-1):
      num -= (i+1)**i
  return num
n = 1
while n < 100:
  print(sub(n), end=', ')
  n += 1

