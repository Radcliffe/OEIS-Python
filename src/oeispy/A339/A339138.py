# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A339138

a, d = [0], 1
while len(a) < 66:
    if d < 10 and a[-1] % 10 == 0: a.append(d); d += 1
    k = 10
    while k in a or (a[-1]%10) + int(str(k)[1]) != int(str(k)[0]): k += 1
    a.append(k)
print(a) # _Dominic McCarty_, Jun 15 2025

