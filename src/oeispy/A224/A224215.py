# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A224215

for a in range(99):
  n = a*a*a
  k = 0
  for x in range(99):
    s = x*x*x
    if s>n: break
    for y in range(99):
        sy = s + y*y*y
        if sy>n: break
        for z in range(99):
            sz = sy + z*z*z
            if sz>n: break
            k+=1
  print(k, end=',')

