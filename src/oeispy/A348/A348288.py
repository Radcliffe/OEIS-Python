# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348288

def count_overlaps(subs, s):
    c = i = 0
    while i != -1:
        i = s.find(subs, i)
        if i != -1: c += 1; i += 1
    return c
def aupton(terms):
    alst, astr, numtocount = [0], "0", 0
    for n in range(2, terms+1):
        c = count_overlaps(str(numtocount), astr)
        numtocount = 0 if c == 0 else numtocount + 1
        alst.append(c)
        astr += str(c)
    return alst
print(aupton(95)) # _Michael S. Branicky_, Oct 10 2021

