"""
Karatsuba multiplication algorithm

Recursive divide-and-conquer method for multiplying large integers.

Time complexity:
    O(n^{log₂ 3}) ≈ O(n^1.585)
"""

def karatsuba(x: str, y: str) -> int:
    n = max(len(x), len(y))

    if n == 1:
       return int(x) * int(y)

    # Pad numbers to equal length
    x = x.zfill(n)
    y = y.zfill(n)

    # Make length even
    if n % 2 != 0:
        n += 1
        x = x.zfill(n)
        y = y.zfill(n)

    # Split into halves
    z = n//2
    a = x[:z]
    b = x[z:]
    c = y[:z]
    d = y[z:]

    # Compute sums
    p = int(a) + int(b)
    q = int(c) + int(d)

    # Recursive products
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    pq = karatsuba(str(p), str(q))

    # Compute cross terms
    adbc = pq - ac - bd

    # Combine results
    return 10 ** n * ac + 10 ** z * adbc + bd

if __name__ == "__main__":
    # Tests
    assert karatsuba("3", "4") == 12
    assert karatsuba("12", "34") == 408
    assert karatsuba("1234", "5678") == 7006652

    x = "3141592653589793238462643383279502884197169399375105820974944592"
    y = "2718281828459045235360287471352662497757247093699959574966967627"

    result = karatsuba(x, y)

    # Final check
    assert result == int(x) * int(y)

    print(result)