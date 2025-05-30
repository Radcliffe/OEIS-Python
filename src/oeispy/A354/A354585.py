# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354585

import sympy
def get_longest_run_of_primes(p):
    run = [p]
    x = 2
    while True:
        next_prime = 2**x - 2 + p
        if sympy.isprime(next_prime):
            run.append(next_prime)
            x = x + 1
        else:
            break
    return run
n_to_longest_run_map = {}
max_prime_index = 100000
for prime_index in range(1, max_prime_index+1):
    p = sympy.prime(prime_index)
    longest_run_for_p = get_longest_run_of_primes(p)
    length_of_longest_run_for_p = len(longest_run_for_p)
    if length_of_longest_run_for_p not in n_to_longest_run_map:
        n_to_longest_run_map[length_of_longest_run_for_p] = longest_run_for_p
n = 1
seq = []
while n in n_to_longest_run_map:
    seq.append(n_to_longest_run_map[n][0])
    n = n + 1
print(seq)

