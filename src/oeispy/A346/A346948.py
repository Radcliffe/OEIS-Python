# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A346948

from sympy import isprime; from math import sqrt, ceil
def neib(m):
    if m == 1: return [3, 5, 7, 9, 11, 13]
    if m == 3: return [17, 19, 5, 1, 13, 15]
    L = [m for i in range(6)]; n = int(ceil((3+sqrt(6*m + 3))/6)); x=6*n*n; y=12*n
    a0 = x-18*n+15; a1 =x-16*n+11; a2 =x-14*n+9
    a3 = x-y+7; a4 =x-10*n+5; a5 =x-8*n+3; a6 =x-6*n+1
    p = 0 if m==a0 else 1 if m>a0 and m<a1 else 2 if m==a1 else 3 if m>a1 and m<a2 else 4 if m==a2 else 5 if m>a2 and m<a3 else 6 if m==a3 else 7 if m>a3 and m<a4 else 8 if m==a4 else 9 if m>a4 and m<a5 else 10 if m==a5 else 11 if m>a5 and m<a6 else 12
    L[0] += y-10 if p<=4 else -2 if p<=6 else -y+16 if p<=9 else 2
    L[1] += 2 if p<=1 else y-8 if p<=6 else -2 if p<=8 else -y+14
    L[2] += -y+24 if p<=1 else 2 if p<=3 else y-6 if p<=8 else -2 if p<=10 else -y+12
    L[3] += -2 if p==0 else -y+22 if p<=3 else 2 if p<=5 else y-4 if p<=10 else -2
    L[4] += y-14 if p==0 else -2 if p<=2 else -y+20 if p<=5 else 2 if p<=7  else y-2
    L[5] += y-12 if p<=2 else -2 if p<=4 else -y+18 if p<=7 else 2 if p<=9  else y
    return L
for i in range(1, 1500):
    m = 2*i - 1
    if isprime(m) == 1:
        L1 = [neib(m)[j] for j in range(6)]
        if sum(isprime(k) for k in L1) == 0: print(m)

