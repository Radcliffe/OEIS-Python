# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A182182

prpr = 0
prev = 1
print('0,1', end=',')
for i in range(2,101):
    current = prev ^ prpr ^ i
    print(current, end=",")
    prpr = prev
    prev = current

