# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A295005

def aupto(limit):
  alst = []
  for k in range(1, limit+1):
    if max(str(k*k)) == "5": alst.append(k)
  return alst
print(aupto(1050)) # _Michael S. Branicky_, May 15 2021

