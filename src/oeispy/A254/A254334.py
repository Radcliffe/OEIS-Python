# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A254334

def digits(n,b=10): # list of digits of n in base b
    x, y = n, []
    while x >= b:
        x, r = divmod(x,b)
        y.append(r)
    y.append(x)
    return list(reversed(y))
A254334_list = [int(''.join([format(x,'02d') for x in digits(3**i, 60)])) for i in range(10**2)]
# _Chai Wah Wu_, Mar 14 2015

