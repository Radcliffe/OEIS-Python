# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A239071

def isqrt(a):
    sr = 1 << (int.bit_length(int(a)) >> 1)
    while a < sr*sr:  sr>>=1
    b = sr>>1
    while b:
        s = sr + b
        if a >= s*s:  sr = s
        b>>=1
    return sr
def isTriang(x):
    x+=x
    r = isqrt(x)
    return r*(r+1)==x
print('0', end=', ')
for n in range(777):
    tn = n*(n+1)//2
    tn1 = (n+1)*(n+2)//2
    for t in range(tn+1, tn1+1):
        if isTriang(tn+t+tn1): print(str(t), end=',')

