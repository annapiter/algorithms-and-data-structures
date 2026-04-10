"""
Count inversions in an array using two approaches:

1. Naive approach (O(n^2))
2. Merge-based approach (O(n log n))

Performance (inversion_input_100k.txt):
- Naive: 2407905288 inversions, ~300.50 seconds
- Merge-based: 2407905288 inversions, ~0.33 seconds
"""

import time
import numpy as np

# load test data (100k integers)
data = np.loadtxt('inversion_input_100k.txt', dtype=int).tolist()

# 1. Count inversions using brute-force (O(n^2))
def count_inversions_naive(A):
    n = len(A)
    k = n // 2

    leftInv = 0
    rightInv = 0
    splitInv = 0

    # count inversions within left half
    for i in range(k-1):
        for j in range(i + 1, k):
            if A[i] > A[j]:
                leftInv += 1

    # count inversions within right half
    for i in range(k, n-1):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                rightInv += 1

    # count split inversions (left vs right)
    for i in range(k):
        for j in range(k, n):
            if A[i] > A[j]:
                splitInv += 1

    total_inv = leftInv + rightInv + splitInv

    return total_inv


# 2. Count inversions using divide-and-conquer (merge sort)
def count_inversions_merge(A):
    n = len(A)

    # base case: no inversions in array of size 0 or 1
    if n <= 1:
        return (A, 0)

    else:
        # divide: split array into two halves
        C, D = A[:n // 2], A[n // 2:]

        # recursively count inversions in left and right halves
        (left_split, leftInv) = count_inversions_merge(C)
        (right_split, rightInv) = count_inversions_merge(D)

        # merge step: count split inversions
        i = 0
        j = 0
        splitInv = 0
        B = []

        while i < len(left_split) and j < len(right_split):
            if left_split[i] <= right_split[j]:
                B.append(left_split[i])
                i += 1
            else:
                B.append(right_split[j])
                j += 1
                # all remaining elements in left_split form inversions
                splitInv += len(left_split) - i

        # append remaining elements
        B.extend(left_split[i:])
        B.extend(right_split[j:])

        # total inversions = left + right + split
        return(B, leftInv + rightInv + splitInv)

# 3. Compare running time of two implementations
start = time.perf_counter()
inv_count1 = count_inversions_naive(data)
end = time.perf_counter()
print("Naive. Number of inversions = ", inv_count1)
print(f"Naive Running time: {end - start:.6f} seconds")

start = time.perf_counter()
sorted_A, inv_count = count_inversions_merge(data)
end = time.perf_counter()
print("Merge. Number of inversions =", inv_count)
print(f"Merge Running time: {end - start:.6f} seconds")