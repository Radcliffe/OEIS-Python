# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A260348

def sod(n,m):
    kk = 0
    while n > 0:
        kk= kk+(n%m)
        n =int(n//m)
    return kk
for c in range (1, 10**6):
    k=len(str(sod(c,10)))
    kl=10**k-sod(c,10)
    if c%kl==0:
        print (c)

