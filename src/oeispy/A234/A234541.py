# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A234541

primes = [2, 3]
primFlg = [0]*100000
primFlg[2] = primFlg[3] = 1
def appPrime(k):
  for p in primes:
    if k%p==0:  return
    if p*p > k:  break
  primes.append(k)
  primFlg[k] = 1
for n in range(5, 100000, 6):
  appPrime(n)
  appPrime(n+2)
for n in range(1, 100000):
  a = 0
  for k in range(1, n):
    c = n//k + n%k
    if primFlg[c]:  # if c in primes:
      a = k
      break
  print(str(a), end=', ')

