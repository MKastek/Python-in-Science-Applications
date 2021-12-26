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
    return n, fib

if __name__ == '__main__':
    start = time.time()
    pool = ProcessPoolExecutor(2)
    fs = [pool.submit(worker,n) for n in range(20)]
    rs = [f.result() for f in fs]
    stop = time.time()
    print(f'{stop - start = }')
    print(rs)
