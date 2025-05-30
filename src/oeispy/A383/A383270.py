# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383270

def a(n):
    if n == 0: return 1
    if n.bit_length() == n.bit_count(): return n.bit_length()
    c = p = m = 0
    while n:
        if n & 1: c += 1
        else:
            p = c * ((n & 2) > 0)
            c = 0
        if (pc := p + c) > m: m = pc
        n >>= 1
    return m + 1
print([a(n) for n in range(1,88)])

