from itertools import permutations
import math
from time import time

def is_pandigital(n):
    return sorted(str(n)) == ['0','1','2','3','4','5','6','7','8','9']

def smallest_pandigitals(n=5):
    digits = '1023456789'
    count = 0
    results = []
    for perm in permutations(digits):
        if perm[0] != '0':  # Ensure 10 digits
            num = int(''.join(perm))
            results.append(num)
            count += 1
            if count == n:
                break
    return sorted(results)

def divisible_pandigitals():
    results = []
    start_time = time()
    for perm in permutations('0123456789'):
        if perm[0] == '0':
            continue
        num = int(''.join(perm))
        if all(num % i == 0 for i in range(1, 10)):
            results.append(num)
            if len(results) == 2: #Delete this line to get all results
                break
    end_time = time()
    return results, end_time - start_time

def divisible_pandigitals_optimized():
    results = []
    start_time = time()
    for perm in permutations('0123456789'):
        if perm[0] == '0':
            continue
        num = int(''.join(perm))
        if num % 2520 == 0:
            results.append(num)
    end_time = time()
    return results, end_time - start_time

def pandigital_squares():
    results = []
    start_time = time()
    for perm in permutations('0123456789'):
        if perm[0] == '0':
            continue
        num = int(''.join(perm))
        root = int(math.isqrt(num))
        if root * root == num:
            results.append(num)
            if len(results) == 2:  #Delete this line to get all results
                break
    end_time = time()
    return results, end_time - start_time

def pandigital_squares_optimized():
    results = []
    start_time = time()
    min_root = math.isqrt(1023456789)  # sqrt of smallest pandigital
    max_root = math.isqrt(9876543210)  # sqrt of largest pandigital
    for root in range(min_root, max_root + 1):
        square = root * root
        if is_pandigital(square):
            results.append(square)
    end_time = time()
    return results, end_time - start_time

# 1. Five pandigitals
print("\n1. Smallest five pandigital numbers:")
smallest_five = smallest_pandigitals(5)
for num in smallest_five:
    print(num)

# 2 & 3. Divisible Pandigitals
print("\n2 & 3. Pandigital numbers divisible by 1-9:")
print("1st force approach:")
divisible_1st, time_1st = divisible_pandigitals()
print(f"Results: {divisible_1st}")
print(f"Total results: {len(divisible_1st)}")
print(f"Time taken by 1st Method: {time_1st:.2f} seconds")

print("\nOptimized approach (using 2520):")
divisible_opt, time_opt = divisible_pandigitals_optimized()
print(f"Results: {divisible_opt}")
print(f"Total results: {len(divisible_opt)}")
print(f"Time taken by Optimized Method: {time_opt:.2f} seconds")

# 4 & 5. Square Pandigitals
print("\n4 & 5. Pandigital squares:")
print("1st approach:")
squares_1st, time_1st = pandigital_squares()
print(f"Results: {squares_1st}")
print(f"Total results: {len(squares_1st)}")
print(f"Time taken: {time_1st:.2f} seconds")

print("\nOptimized approach:")
squares_opt, time_opt = pandigital_squares_optimized()
print(f"Results: {squares_opt}")
print(f"Total results: {len(squares_opt)}")
print(f"Time taken: {time_opt:.2f} seconds")
print("\n")