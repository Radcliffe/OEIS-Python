# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A297815

import math
def digitProd(natNumber):
    digitProd = 1
    for letter in str(natNumber):
        digitProd *= int(letter)
    return digitProd
def digitSum(natNumber):
    digitSum = 0
    for letter in str(natNumber):
        digitSum += int(letter)
    return digitSum
for n in range(24):
    count = 0
    for a in range(int(math.pow(10,n)), int(math.pow(10, n+1))):
        if digitProd(a) == digitSum(a):
            count += 1
    print(n+1, count)

