# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A216267

def rootPronic(a):
    sr = 1<<33
    while a < sr*(sr+1):
      sr>>=1
    b = sr>>1
    while b:
        s = sr+b
        if a >= s*(s+1):
          sr = s
        b>>=1
    return sr
for i in range(1<<20):
      a = i*(i+1)*(i+2)//6
      t = rootPronic(a)
      if a == t*(t+1):
        print(a)

