# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A305191

[[len([(x, y) for x in range(n) for y in range(n) if (pow(x,2,n)+pow(y,2,n))%n==d]) for d in range(n)] for n in range(1,10)]

