def rational(x, y):
    gcd_rational = gcd(x, y)
    return [x // gcd_rational, y // gcd_rational]

def denom(r):
    return r[1]

def numer(r):
    return r[0]

def mul_rational(r1, r2):
    return rational(numer(r1) * numer(r2), denom(r1) * denom(r2))

def add_rational(r1, r2):
    return rational(numer(r1) * denom(r2) + numer(r2) * denom(r1), \
                    denom(r1) * denom(r2))

def print_rational(r):
    print(numer(r), '/', denom(r)) 

def gcd(a, b):
    """
    >>> gcd(12, 14)
    2
    >>> gcd(27, 18)
    9
    >>> gcd(12, 12)
    12
    """
    if a == 0:
        return b
    else:
        return gcd(b % a, a)
