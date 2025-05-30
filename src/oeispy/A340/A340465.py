# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340465

from sympy import isprime, nextprime, prime
def sp2(lst):
  ans = 0
  for i in range(0, len(lst), 2): ans += lst[i]*lst[i+1]
  return ans
def aupto(nn):
  alst, i = [], 1
  while True:
    consec2i = [prime(j+1) for j in range(2*i)]; sp = sp2(consec2i)
    if sp > nn: break
    while sp <= nn:
      if isprime(sp): alst.append(sp)
      consec2i = consec2i[1:] + [nextprime(consec2i[-1])]; sp = sp2(consec2i)
    i += 1
  return sorted(alst)
print(aupto(261983)) # _Michael S. Branicky_, Jan 08 2021

