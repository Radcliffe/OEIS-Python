# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A287837

def a(n):
 if n in [0,1,2]:
  return [1, 11, 113][n]
 return 10*a(n-1) + 3*a(n-2)

