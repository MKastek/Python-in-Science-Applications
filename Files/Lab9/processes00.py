import multiprocessing as mp
import time
import os
# pula procesów
from concurrent.futures import ProcessPoolExecutor

index = 0

def fibon(n):
    if n < 2:
        return n
    return fibon(n - 1) + fibon(n - 2)

def worker(n):
    fib = fibon(n)
    print(f'Calc: {n} -> {fib}')
    return fib

start = time.time()
for n in range(20):
    worker(n)
stop = time.time()
print(f'{stop - start = }')