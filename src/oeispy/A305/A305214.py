# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A305214

[n for n in range(100) if n != len(set((pow(x,3,n) + pow(y,3,n))%n for x in range(n) for y in range(n)))]

