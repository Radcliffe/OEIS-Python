# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367338

from itertools import islice
def a(n):
    an, y = n, 1
    while y < 10:
        an, y = an + 10*(an%10), 1
        while y < 10:
            if str(an+y)[0] == str(y):
                an += y
                break
            y += 1
        if y < 10:
            return an
    return -1
print([a(n) for n in range(1, 66)]) # _Michael S. Branicky_, Nov 15 2023

