# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A344888

def A344888(n):
    b, m = 2, n
    while True:
        m, x = divmod(m, b)
        m, y = divmod(m, b)
        while m > 0:
            m, z = divmod(m,b)
            if z != x:
                break
            if m > 0:
                m, z = divmod(m,b)
                if z != y:
                    break
            else:
                return b
        else:
            return b
        b += 1
        m = n # _Chai Wah Wu_, Jun 02 2021

