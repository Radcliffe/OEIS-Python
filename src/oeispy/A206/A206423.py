# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A206423

alst, terms = [12, 7], 37
[alst.append(alst[n-1] + alst[n-2]) for n in range(2, terms)]
print(alst) # _Michael S. Branicky_, Dec 07 2021

