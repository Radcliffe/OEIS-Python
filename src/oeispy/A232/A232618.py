# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A232618

o=e=1
for n in range(1,99,2):
  o*=n
  e*=n+1
  print(str(e%o), end=',')

