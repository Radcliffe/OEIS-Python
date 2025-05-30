# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A336912

from math import floor, sqrt
def a(n):
    if n == 1: return 0
    count = 0
    while True:
        if (n % 2) == 0: n = int(floor(sqrt(n)))
        else: n = n**3 + 1
        count += 1
        if n == 1: break
    return count
print([a(n) for n in range(1, 101)])

