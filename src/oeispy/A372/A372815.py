# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A372815

def factors(n):
    return sorted([i for i in range(2, n - 1) if n % i == 0])
def main():
    for i in range(1, 20):
        fs = factors(i)
        if len(fs) == 0:
            l = 0
        else:
            l = fs[-1]
        print(i*i - l)
if __name__ == "__main__":
    main()

