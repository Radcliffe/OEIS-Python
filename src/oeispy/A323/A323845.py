# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A323845

def a(n) :
  k = (n-1)//2;
  return 3**k*((3**k+1) if n&1 else (3**(k+1)+5))//2 if n else 1;

