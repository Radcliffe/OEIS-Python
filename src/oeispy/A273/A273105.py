# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A273105

print('0', end=',')
for n in range(1,1000):
    BL = len(bin(n))-2
    x = (n>>1) + ((n&1) << (BL-1))   # A038572(n)
    x+= (n*2) - (1<<BL) + 1   # A006257(n)  for n>0
    print(str(x), end=',')

