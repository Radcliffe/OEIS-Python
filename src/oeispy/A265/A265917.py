# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A265917

for n in range(1, 88):
    print(str((len(bin(n))-2) // bin(n).count('1')), end=',')

