# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A185826

num = 100
n = 0
a = []
for i in range(1, num):
    sum = 0
    for j in range(1, i+1):
        sum = sum + (n+j)
    n = n + i
    a.append(sum**i)

