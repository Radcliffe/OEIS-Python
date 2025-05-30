# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A197123

# download https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt, then
# with open('pi-billion.txt', 'r') as f: digits_of_pi = f.readline()
from sympy import S; digits_of_pi = str(S.Pi.n(3*10**5)) # alternatively
def a(n):
  global digits_of_pi
  seen = set()
  for i in range(2, len(digits_of_pi)-n):
    ss = digits_of_pi[i:i+n]
    if ss in seen: return int(ss)
    seen.add(ss)
for n in range(1, 11):
  print(a(n), end=", ") # _Michael S. Branicky_, Jan 26 2021

