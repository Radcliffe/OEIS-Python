# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364479

def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
def is_palindrome(num):
    return str(num) == str(num)[::-1]
def is_happy(num):
    while num != 1 and num != 4:
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1
happy_palindromic_primes = [num for num in range(1, 10000000) if is_prime(num) and is_palindrome(num) and is_happy(num)]
print(happy_palindromic_primes)

