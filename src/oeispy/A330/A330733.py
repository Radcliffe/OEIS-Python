# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A330733

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper
@memoize
def unique_factors_of(n):
    factors = []
    for candidate in range(2, n//2 + 1):
        if n % candidate == 0:
            factors.append(candidate)
    return factors
@memoize
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True
@memoize
def rhythm(n):
    if n == 0:
        return [0]
    natural_rhythm_of_n = [0]*(n-1)
    natural_rhythm_of_n += [1]
    if is_prime(n):
        return natural_rhythm_of_n
    else:
        component_rhythms = [natural_rhythm_of_n]
        for divisor in unique_factors_of(n):
            component_rhythm = n//divisor * rhythm(divisor)
            component_rhythms.append(component_rhythm)
        return [sum(i) for i in zip(*component_rhythms)]
for i in range(0, 201):
    formatted_string = f'{str(i).rjust(3)}|'
    for note in rhythm(i):
        formatted_string += f'{str(note).rjust(4)}'
    print(formatted_string)

