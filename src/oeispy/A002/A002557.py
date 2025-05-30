# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A002557

powerset = lambda lst: reduce(lambda result, x: result + [subset + [x] for subset in result], lst, [[]])
product = lambda lst: reduce(lambda x, y: x*y, lst, 1)
primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
sequence = sorted(product(s) for s in powerset(primes) if len(s) % 2 == 0) # _David Radcliffe_, Jan 21 2016

