# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A239137

is_ok = lambda s: not any(s[i-2] <= s[i-1] <= s[i] for i in range(2, len(s)))
terms, appears, digits = [1], {1}, '1'
for i in range(100):
    t = 1
    while not(
        t not in appears
        and is_ok(digits + str(t))
        and t % 100 not in [0, 1, 11]
    ): t += 1
    terms.append(t); appears.add(t); digits = digits + str(t)
    digits = digits[-2:]
print(terms) # _Gleb Ivanov_, Dec 06 2021

