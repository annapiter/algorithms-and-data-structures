"""
QuickSort implementations with three pivot strategies:

1. First element as pivot
2. Last element as pivot
3. Median-of-three pivot

The program counts the total number of comparisons for each version.
"""
import numpy as np

# 1. First element pivot
def quick_sort_first_pivot(A, l, r):
    if r - l <= 1:
        return 0 # base case: no comparisons

    # number of comparisons in this call
    comparisons = r - l - 1

    # choose pivot as the first element
    p = A[l]
    i = l + 1

    for j in range(l + 1, r):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1

    # place pivot in correct position
    A[l], A[i-1] = A[i-1], A[l]

    # recurse on left part
    comparisons += quick_sort_first_pivot(A, l, i - 1)

    # recurse on right part
    comparisons += quick_sort_first_pivot(A, i, r)

    return comparisons


# 2. Last element pivot
def quick_sort_last_pivot(A, l, r):
    if r - l <= 1:
        return 0 # base case: no comparisons

    # number of comparisons in this call
    comparisons = r - l - 1

    # choose the last element as pivot and move it to the first position
    A[r - 1], A[l] = A[l], A[r-1]
    p = A[l]
    i = l + 1

    for j in range(l + 1, r):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1

    # place pivot in correct position
    A[l], A[i - 1] = A[i - 1], A[l]

    # recurse on left part
    comparisons += quick_sort_last_pivot(A, l, i - 1)

    # recurse on right part
    comparisons += quick_sort_last_pivot(A, i, r)

    return comparisons


# 3. Median-of-three pivot
def quick_sort_median_of_three(A, l, r):
    if r - l <= 1:
        return 0 # base case: no comparisons

    # choose pivot as the median of three:
    # first, middle, and last element of the current subarray A[l:r]
    m = l + (r - 1 - l) // 2

    candidates = [A[l], A[m], A[r - 1]]
    candidates.sort()
    p = candidates[1]

    # number of comparisons in this call
    comparisons = r - l - 1

    # move chosen pivot to the first position
    if p == A[m]:
        A[m], A[l] = A[l], A[m]
    elif p == A[r - 1]:
        A[r - 1], A[l] = A[l], A[r - 1]

    p = A[l]
    i = l + 1

    for j in range(l + 1, r):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1

    # place pivot in correct position
    A[l], A[i - 1] = A[i - 1], A[l]

    # recurse on left part
    comparisons += quick_sort_median_of_three(A, l, i - 1)

    # recurse on right part
    comparisons += quick_sort_median_of_three(A, i, r)

    return comparisons


# Load test data (10k integers)
data = np.loadtxt('quick_sort_input_10k.txt', dtype=int).tolist()

A1 = data.copy()
print("QuickSort (first pivot): comparisons =", quick_sort_first_pivot(A1, 0, len(A1)))

A2 = data.copy()
print("QuickSort (last pivot): comparisons =", quick_sort_last_pivot(A2, 0, len(A2)))

A3 = data.copy()
print("QuickSort (median-of-three): comparisons =", quick_sort_median_of_three(A3, 0, len(A3)))
