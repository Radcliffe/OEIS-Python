# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A300783

# see A159842 for the definitions of dc, fin, per, u, N, N2
def a(n):
    return (dc(u, N, N2)(n) + 6*dc(fin(1, -1, 0, 4), u, u, N)(n)
            + dc(fin(1, 3), u, u, N)(n)
            + 4*dc(fin(1, 0, 1), u, u, per(0, 1, -1))(n)) // 12
print([a(n) for n in range(1, 100)])
# _Andrey Zabolotskiy_, Feb 03 2020

