# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A382630

# returns the first 100 terms as a list
import numpy as np
terms = 100
a = np.zeros(terms)
for d in range(3,terms // 2):
    for c in range(2,d):
        for b in range(1,c):
            val = b + c*d
            if val < terms:
                a[val] += 1
print(a)

