# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355916

from collections import Counter
def aupton(terms):
    num, alst, inventory = 0, [0, 0], Counter([0, 0])
    for n in range(3, 3+terms//2):
        c = [inventory[num], num]
        num = 0 if c[0] == 0 else num + 1
        alst.extend(c)
        inventory.update(c)
    return alst[:terms]
print(aupton(128)) # _Michael S. Branicky_, Sep 25 2022

