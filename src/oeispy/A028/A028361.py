# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A028361

for n in range(2,50,2):
  product = 1
  for i in range(0,n//2-2 + 1):
    product *= (2**i+1)
  print(product)
# _Nathan J. Russell_, Mar 01 2016

