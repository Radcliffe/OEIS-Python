# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355774

def A355774_list(upto: int) -> list[int]:
    P: list[int] = []
    for k in range(upto + 1):
        if any(
            k == ((n + n % 2) * (3 * n + 2 - n % 2)) >> 3
            for n in range(k + 1)
        ) or not any([(k - p) in P for p in P]):
            P.append(k)
    return P
print(A355774_list(448))

