# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370377

a = [1, 3, 2, 6, 5, 14]
for i in range(30):
    a.append(2*a[-2]+a[-4]-a[-6])
print(a)

