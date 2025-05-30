# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A368136

def containsloops(k):
    for x_ in range(k, k*k):
        s = 0
        x = x_
        m = x
        while x != 1 and s <= m:
            d, r = divmod(x, k)
            x = d if r == 0 else d + x + 1
            s += 1
            m = max(m, x)
        if s > m and x > k:
            return True
    return False
print([k for k in range(1, 100) if containsloops(k)])

