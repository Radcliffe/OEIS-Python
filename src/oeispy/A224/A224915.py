# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A224915

for n in range(59):
    s = 0
    for k in range(n):  s += n ^ k
    print(s, end=',')

