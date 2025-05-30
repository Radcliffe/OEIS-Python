# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349493

from math import gcd
terms, appears = [1, 2], {2:True}
for n in range(3, 100):
    t = 3
    while not(appears.get(t) is None and gcd(terms[-2]+terms[-1], t)>1 and gcd(terms[-2], t)==1 and gcd(terms[-1], t)==1):
        t += 1
    appears[t] = True; terms.append(t);
print(terms) #_Gleb Ivanov_, Nov 20 2021

