# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A305211

[len(set((pow(x,3,n)+pow(y,3,n))%n for x in range(n) for y in range(x+1))) for n in range(1,51)]

