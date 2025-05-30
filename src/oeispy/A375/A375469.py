# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375469

def A375469row(n: int) -> list[int]:
    t = n * (n + 1) // 2
    return [A375825row(n + 1)[k + 1] + t - 1 for k in range(n + 1)]
print([A375469row(n)[k] for n in range(11) for k in range(n + 1)])

