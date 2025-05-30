# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A280191

def a(n):
    if n > 14:
        if n%2 == 1:
            return 2**((n-1)/2) - n*(n-1)/2
        if n%4 == 2:
            return 2**((n-2)/2) - n*(n-1)/2
        if n%4 == 0:
            return 2**((n-2)/2) - n*(n-1)/2 + biggestdivisor(n,2)
    elif n >= 5:
        return [0,0,4,5,5,4,5,6,6,7][n-5]
    return "Error"
def biggestdivisor(n,d): # return largest power of d dividing n
    if n%d != 0:
        return 1;
    else:
        return d*biggestdivisor(n/d, d);

