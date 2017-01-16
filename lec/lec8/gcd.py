def gcd(m, n):
    """
    m, n being positive integers, giving back the greatest common divider
    >>> gcd(12, 18)
    6
    >>> gcd(36, 24)
    12
    >>> gcd(5, 5)
    5
    >>> gcd(18, 2)
    2
    >>> gcd(2, 12)
    2
    """
    if m == 0:
        return n
    else:
        return gcd(n % m, m)
