# The second part (see details in README.md)
import time
import multiprocessing

def calculate_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def factorize_synchronized(*numbers):
    factors = []
    for num in numbers:
        factors.append([i for i in range(1, num + 1) if num % i == 0])
    return factors

def factorize_parallel(*numbers):    
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        factors = pool.map(calculate_factors, numbers)
    return factors

# Testing the synchronized version
start_time = time.time()
a, b, c, d = factorize_synchronized(128, 255, 99999, 10651060)
sync_time = time.time() - start_time

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

print(f"Synchronized execution time: {sync_time:.4f} seconds")

# Testing the parallel version
start_time = time.time()
a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
parallel_time = time.time() - start_time

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

print(f"Parallel execution time: {parallel_time:.4f} seconds")
