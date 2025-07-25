# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A385493

import torch
import numpy as np
def prime_mask(limit):
    is_prime = torch.ones(limit + 1, dtype=torch.bool)
    is_prime[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i : limit+1 : i] = False
    return is_prime
def Gauss_primes(N):
    A, B = torch.meshgrid(torch.arange(-N, N+1), torch.arange(-N, N+1))
    norm = A**2 + B**2
    is_prime = prime_mask(2*N**2)
    mask = (A != 0) & (B != 0) & is_prime[norm]
    axis_mask = ((A == 0) ^ (B == 0))
    axis_val = (A + B).abs()
    axis_mask &= is_prime[axis_val] & ((axis_val % 4) == 3)
    return mask | axis_mask
def update(G):
    shifts = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    neighbors = sum(torch.roll(G, shifts=shift, dims=(0,1)) for shift in shifts)
    return (G & ((neighbors == 2) | (neighbors == 3))) | (~G & (neighbors == 3))
def a(n):
    if n == 0 or n == 1:
        return 1
    G = Gauss_primes(n).to("cuda").to(torch.uint8)
    seen, step = set(), 0
    while True:
        flat = G.flatten().to("cpu").numpy()
        key = bytes(np.packbits(flat))
        if key in seen:
            return step
        seen.add(key)
        G = update(G)
        step += 1

