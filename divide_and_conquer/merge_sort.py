"""
Merge sort algorithm

Recursive divide-and-conquer sorting algorithm.

Time complexity:
    O(n log n)
"""
def merge_sort(A):
    n = len(A)

    if n <= 1:
        return A

    else:
        # split array into two halves
        left, right = A[: n//2], A[n//2 :]

        # recursively sort both halves
        left_split = merge_sort(left)
        right_split = merge_sort(right)

        # merge: combine two sorted halves
        i = 0
        j = 0
        sorted_list = []

        while i < len(left_split) and j < len(right_split):
            # take the smaller element
            if left_split[i] <= right_split[j]:
                sorted_list.append(left_split[i])
                i += 1
            else:
                sorted_list.append(right_split[j])
                j += 1

        # append remaining elements
        sorted_list.extend(left_split[i:])
        sorted_list.extend(right_split[j:])

        return sorted_list

A = [5, 4, 1, 8, 7, 2, 6, 3]
print(merge_sort(A))
