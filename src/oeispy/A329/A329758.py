# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A329758

def A329758():
   x = 1
   g = A000002()
   while True:
       yield x
       acc = 0
       for i in range(0, x):
           acc = acc + next(g)
       x = acc # _Jack W Grahl_, May 04 2020

