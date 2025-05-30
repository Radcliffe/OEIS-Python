# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A339616

from sympy import isprime
def aupto(n):
    alst, used, strakm1 = [0, 2], {2}, "2"
    for k in range(2, n+1):
        ball = (str(alst[k-1]))[-1]
        ak = 1
        ball_left = ball + (str(ak))[:-1]
        while isprime(int(ball_left)) or ak in used or not isprime(ak):
            ak += 2 # continue to only test odds
            ball_left = ball + (str(ak))[:-1]
        alst.append(ak)
        used.add(ak)
    return alst[1:]  # use alst[n] for a(n) function
print(aupto(70)) # _Michael S. Branicky_, Dec 11 2020

