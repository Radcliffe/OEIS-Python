# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A384715

def A001316(n): return (1 + (n % 2)) * A001316(n // 2) if n else 1
def A033264(n): return (n % 4 == 2) + A033264(n // 2) if n else 0
def A085357(n): return int(n & (n<<1) == 0)
def A384715(n): return A001316(n) * (A033264(n) - A085357(n) + 2)

