# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A214852

def count10(x):
    c0, c1, m = 0, 0, 1
    while m<=x:
      if x&m:
        c1+=1
      else:
        c0+=1
      m+=m
    return c0-c1
prpr, prev = 0,1
TOP = 1<<16
for i in range(1,TOP):
    if count10(prev)==0:
        print i,
    prpr, prev = prev, prpr+prev

