# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A288023

num = 1
def triangleN(x):
    return x*(x+1)/2
def stepCount(x):
    x = int(x)
    steps = 0
    while True:
        if x == 1:
            break
        elif x % 2 == 0:
            x = x/2
            steps += 1
        else:
            x = x*3 + 1
            steps += 1
    return steps
while True:
    print(stepCount(triangleN(num)))
    num += 1

