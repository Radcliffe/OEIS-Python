# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342265

def nondec(n): s = str(n); return s == "".join(sorted(s))
def aupton(terms):
  alst = [0]
  for n in range(2, terms+1):
    an, cumsum = 1, sum(alst)
    while True:
      while an in alst: an += 1
      if nondec(an) and nondec(cumsum + an): alst.append(an); break
      else: an += 1
  return alst
print(aupton(100)) # _Michael S. Branicky_, Mar 07 2021

