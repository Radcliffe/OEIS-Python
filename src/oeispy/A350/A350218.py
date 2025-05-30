# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350218

from num2words import num2words
def n2w(n): return num2words(n).replace(" and", "")
def aupton(terms):
    alst, aset = [1], {1}
    for n in range(2, terms+1):
        an = 1
        avoid = n2w(alst[-1])[0]
        while an in aset or avoid in n2w(an): an += 1
        alst.append(an); aset.add(an)
    return alst
print(aupton(70)) # _Michael S. Branicky_, Dec 20 2021

