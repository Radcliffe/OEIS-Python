# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A248939

def A248939_row(n):
    seen = {n}; orbit = [n]; c = 0
    while n != 0:
        ++c; s = c if n>0 else -c; n += s if n-s in seen else -s
        seen.add(n); orbit.append(n)
    return orbit # _M. F. Hasler_, Mar 18 2019

