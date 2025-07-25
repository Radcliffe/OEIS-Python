# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A384870

def a(n):
    k = 1
    while True:
        powers = [(i + 1) ** n for i in range(k)]
        subset_sums = set()
        all_unique = True
        for mask in range(1 << k):
            total = sum(powers[i] for i in range(k) if mask & (1 << i))
            if total in subset_sums:
                all_unique = False
                break
            subset_sums.add(total)
        if not all_unique:
            return k - 1
        k += 1
print([a(n) for n in range(9)])

