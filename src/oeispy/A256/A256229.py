# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A256229

def A256229(n):
    y = 1
    for d in reversed(str(n)):
        y = int(d)**y
    return y # _Chai Wah Wu_, Mar 21 2015

