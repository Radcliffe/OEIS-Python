# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A257814

def mod(n,a):
    kk = 0
    while n > 0:
        kk= kk+(n%10)**a
        n =int(n//10)
    return kk
for a in range (1, 10):
    for c in range (1, 10**7):
        if c==a*mod(c,a) and a<mod(c,a):
            print (a,c, mod(c,a))

