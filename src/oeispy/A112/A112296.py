# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A112296

def aupton(terms):
    alst, s = [9], 9
    for n in range(2, terms+1):
        alst.append(int(str(s)[::-1]))
        s += alst[-1]
    return alst
print(aupton(28)) # _Michael S. Branicky_, Sep 09 2021

