# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A050425

def ok(n):
    b = bin(n)[2:]
    if b == b[::-1]: return False
    for skip in range(len(b)):
        newb = b[:skip] + b[skip+1:]
        if len(newb) > 0 and newb[0] == '1' and newb == newb[::-1]:
            return True
    return False
print(list(filter(ok, range(172)))) # _Michael S. Branicky_, Aug 24 2021

