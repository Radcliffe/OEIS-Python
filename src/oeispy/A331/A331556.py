# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A331556

# Slow Brute-force
n = 196
while n < 10**15:
  m = n
  while m != int(str(m)[::-1]): m+=-1
  print(n-m, end=', ')
  n = n + int(str(n)[::-1])

