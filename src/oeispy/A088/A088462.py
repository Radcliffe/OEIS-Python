# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A088462

l=[0, 1, 1]
for n in range(3, 101): l.append(n - l[n - 1] - l[l[n - 2]])
print(l[1:]) # _Indranil Ghosh_, Jun 24 2017, after _Altug Alkan_

