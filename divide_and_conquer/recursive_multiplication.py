"""
Recursive integer multiplication algorithm

Recursive divide-and-conquer method for multiplying two large integers
by splitting each number into halves and combining four recursive products.

Time complexity:
    O(n^2)
"""
def rec_int_mult(x: str, y: str) -> int:
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
    z = n // 2
    a = x[:z]
    b = x[z:]
    c = y[:z]
    d = y[z:]

    # Recursive products
    ac = rec_int_mult(a, c)
    ad = rec_int_mult(a, d)
    bc = rec_int_mult(b, c)
    bd = rec_int_mult(b, d)

    # Combine results
    return 10**n * ac + 10**z * (ad + bc) + bd

if __name__ == "__main__":
    # simple tests
    assert rec_int_mult('1', '2') == 2
    assert rec_int_mult('12', '34') == 408
    assert rec_int_mult('1234', '5678') == 1234 * 5678

    # assignment numbers
    x = "3141592653589793238462643383279502884197169399375105820974944592"
    y = "2718281828459045235360287471352662497757247093699959574966967627"

    result = rec_int_mult(x, y)

    assert result == int(x) * int(y)

    print("Result:", result)
    print("Matches Python:", result == int(x) * int(y))

