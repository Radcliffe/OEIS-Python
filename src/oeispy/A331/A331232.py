# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A331232

def fact(num):
    ret = []
    temp = num
    div = 2
    while temp > 1:
        while temp % div == 0:
            ret.append(div)
            temp //= div
        div += 1
    return ret
def all_partitions(lst):
    if lst:
        x = lst[0]
        for partition in all_partitions(lst[1:]):
            yield [x] + partition
            for i, _ in enumerate(partition):
                partition[i] *= x
                yield partition
                partition[i] //= x
    else:
        yield []
best = 0
terms = [0]
q = 2
while len(terms) < 100:
    total_set = set()
    factors = fact(q)
    total_set = set(tuple(sorted(x)) for x in all_partitions(factors) if len(x) == len(set(x)))
    if len(total_set) > best:
        best = len(total_set)
        terms.append(best)
        print(q,best)
    q += 2#only check evens
print(terms)
#  _David Consiglio, Jr._, Jan 14 2020

