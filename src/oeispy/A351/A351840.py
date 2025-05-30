# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A351840

def aupton(terms):
    alst, aset, minunused = [1], {1}, 2
    while len(alst) < terms:
        an = minunused
        while an in aset or (alst[-1]+an)%int(str(an)[0]): an += 1
        alst.append(an); aset.add(an)
        while minunused in aset: minunused += 1
    return alst
print(aupton(100)) # _Michael S. Branicky_, Feb 21 2022

