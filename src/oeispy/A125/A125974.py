# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A125974

def A125974(n):
    if 0 == n:
        return n
    chosen = A000265(n)  # Initially ones, get rid of lsb-0's.
    others = n >> A007814(n + 1)  # Initially zeros, get rid of lsb-1's.
    s = 0  # the resulting sum
    b = n % 2  # n's parity.
    p = 1  # powers of two.
    while (chosen != 0) or (others != 0):
        if (1 == chosen) or (1 == A036987(chosen + 1)):  # Last one or zero at hand.
            chosen = others
            others = 0
            nb = 1 - b
        elif (0 == (chosen % 4)) or (
            3 == (chosen % 4)
        ):  # Source run continues, dest changes.
            tmp = chosen
            chosen = others
            others = tmp >> 1
            nb = 1 - b
        elif 1 == (
            chosen % 4
        ):  # Source run changes, from ones to zeros, skip past zeros.
            chosen = A000265(chosen - 1)
            nb = b
        else:  # Source run changes, from zeros to ones, skip past ones.
            chosen = chosen >> A007814(chosen + 2)
            nb = b
        s += b * p
        p <<= 1
        b = nb
    return s

