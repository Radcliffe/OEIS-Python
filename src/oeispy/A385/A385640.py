# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A385640

def digit_sum(n): return sum(int(d) for d in str(n))
def ok(n):
    return n % digit_sum(n) == 0 and (n**2) % digit_sum(n**2) == 0
print([n for n in range(1, 400) if ok(n)])

