# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A374265

def a(n):
   reach = {1}
   for i in range(1, n+1):
      newreach = set()
      for m in reach:
         newreach.update([m*i, int(str(m*i).replace('0', ''))])
      reach = newreach
   return min(reach)

