# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A114319

noncomp = [0, 1, 2, 3, 5, 7]
terms = [1, 2, 3, 5, 7, 4, 10, 8]
def si(test_list):  # all terms greater than 0 and no repetitions
    a = all(i > 0 for i in test_list)
    b = len(test_list) == len(set(test_list))
    return a & b
def clear(test_list):  # sequence meets definitional criteria
    full = "".join(str(x) for x in test_list)
    for a in test_list:
        if int(a) - 1 >= len(full):
            return True
        elif int(full[int(a) - 1]) not in noncomp:
            return False
    return True
while len(terms) < 100:
    start = 1
    while True:
        terms.append(start)
        if si(terms) and clear(terms):
            break
        else:
            terms.pop()
            start += 1
print(terms)
# _David Consiglio, Jr._, Oct 30 2023

