# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A256516

def a256516():
    best = 1
    yield 1
    i = 2
    while True:
        if i>=len(pi):
            return
        a = pi[i]
        valid = True
        o = 1
        while valid:
            pi_approx = int(pi[:o])
            a_approx = abs(int(pi[i:i+o])-pi_approx)
            b_approx = abs(int(pi[best:best+o])-pi_approx)
            if abs(b_approx-a_approx)>10:
                valid = False
            else:
                o+=1
        if a_approx<b_approx:
            best = i
            yield i
        i+=1

