# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A228126

## sumdivisors(n) is a function that would return the sum of prime
## divisors of n.
i=2
while i < 100000:
  sdi=sumdivisors(i)
  sdip=sumdivisors(i+1)
  if sdi==sdip-1:
    print i,i+1
  i=i+1

