# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A287829

def a(n):
 if n in [0, 1]:
  return [1, 10][n]
 return 9*a(n-1)+2*a(n-2)

