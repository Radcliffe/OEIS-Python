# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342841

import math
for n in range (0, 10):
     counter = 0
     for x in range (1, pow(10, n)+1):
        for y in range(1, pow(10, n)+1):
            for z in range(1, pow(10, n)+1):
                if math.gcd(math.gcd(y, x),z) ==  1:
                    counter += 1
     print(n, counter)

