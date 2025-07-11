# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A385150

def a(n):
    def calc_halting_steps(num, max_steps):
        b = 0
        for step in range(1, max_steps + 1):
            if num % 2 == 0:
                b += 2
            else:
                b -= 1
            num = (3 * num) // 2
            if b < 0:
                return step
        return -1
    a_curr = 0
    while True:
        halting_steps = calc_halting_steps(a_curr, 3 * n + 1)
        if halting_steps == 3 * n + 1:
            return a_curr
        a_curr += 1

