# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358126

def a(n):
    binary_string = "{0:b}".format(n)[::-1]  # little-endian
    result = 0
    for i, binary_digit in enumerate(binary_string):
        if binary_digit == '1':
            result += 1 << (1 << i)  # 2 ** (2 ** i)
    return result

