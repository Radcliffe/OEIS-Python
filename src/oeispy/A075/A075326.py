# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A075326

def aupton(nn):
    alst, disallowed, mink = [0], {0}, 1
    for n in range(1, nn+1):
        nextk = mink + 1
        while nextk in disallowed: nextk += 1
        an = mink + nextk
        alst.append(an)
        disallowed.update([mink, nextk, an])
        mink = nextk + 1
        while mink in disallowed: mink += 1
    return alst
print(aupton(57)) # _Michael S. Branicky_, Jan 31 2022

