# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A214039

ppp =0
prpr=1
prev=2
for n in range(65):
    cur = prev-(prpr+ppp)//2
    print(str(ppp), end=',')
    ppp = prpr
    prpr= prev
    prev= cur

