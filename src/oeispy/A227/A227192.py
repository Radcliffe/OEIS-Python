# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A227192

def A227192(n):
  '''Sum of the partial sums of the run lengths of binary expansion of n, starting from the least significant end.'''
  s = 0
  b = n%2
  i = 0
  while (n != 0):
    n >>= 1
    i += 1
    if((n%2) != b):
      b = n%2
      s += i
  return(s)

