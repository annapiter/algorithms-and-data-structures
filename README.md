# Algorithms and Data Structures

This repository contains my implementations of fundamental algorithms and data structures in Python.

The goal of this project is to strengthen my understanding of algorithmic thinking, recursion, and complexity analysis while studying classic computer science algorithms.

I am currently working through the Stanford / Coursera course:

**Algorithms: Divide and Conquer, Sorting and Searching**  
Instructor: Tim Roughgarden

As I progress through the course, I continuously add implementations of algorithms studied in lectures and programming assignments.

---

## Implemented Algorithms

- Karatsuba Multiplication (Divide and Conquer)
- Recursive Integer Multiplication (Divide and Conquer)
- Merge Sort (O(n log n))
- Inversion Counting:
  - Naive approach (O(n²))
  - Merge-based approach (O(n log n))

---

## Performance Comparison

Inversion counting was tested on a dataset with 100,000 integers:

- Naive approach: ~300.5 seconds  
- Merge-based approach: ~0.33 seconds  

Both implementations produced the same result:

**2,407,905,288 inversions**

The divide-and-conquer approach is approximately **900× faster** than the naive implementation.

---

## Topics Covered

This repository includes implementations of:

- Divide and Conquer
- Sorting algorithms (Merge Sort, QuickSort)
- Graph algorithms (BFS, DFS, shortest paths)
- Dynamic Programming

---

## Project Goals

- Implement algorithms from scratch
- Develop intuition for time complexity and asymptotic analysis
- Build a structured and well-documented algorithm repository
- Prepare for advanced coursework in data science and computer science

---

## Notes

Each algorithm implementation includes:
- Clean, readable Python code
- Inline documentation
- Test cases and performance comparisons (where applicable)

More detailed explanations may be added as separate notes.

---

## License

This project is licensed under the MIT License.