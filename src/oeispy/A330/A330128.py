# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A330128

def nxt(x):
    p, n = 1, x
    while n >= 10:
        n //= 10
        p *= 10
    return p * (n + 1)
def a(n):
    nT, nX, w1, w2, w3, stp  = 1, n, 0, 0, 0, 100
    while True:
        oX = nX
        nT += 1
        x = 10*(oX%10)
        nX = next((y for y in range(1, 10) if str(oX+x+y)[0] == str(y)), 0)
        if nX == 0: break
        else: nX += oX + x
        if nT == stp:
            stp += 100
            w1, w2, w3 = w2, w3, nX
            if w3 + w1 == 2*w2 and (w3 - w2)%100 == 0:
                it = (nxt(nX) - nX - 1)//(w3 - w2)
                nT += it*100
                nX += (w3 - w2)*it
                w3 = nX
                stp += it*100
    return nT - 1
print([a(n) for n in range(1, 30)]) # _Michael S. Branicky_, Nov 18 2023 after _Giovanni Resta_

