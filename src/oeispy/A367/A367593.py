# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367593

def digit_reversal(n):
    return int(str(n)[::-1])
def find_integers():
    result = []
    for k in range(0, 10**10):
        reversed_k = digit_reversal(k)
        if (reversed_k - 1) % (k + 1) == 0:
            result.append(k)
    return result
integers_list = find_integers()
print(integers_list)

