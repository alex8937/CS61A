from fractions import gcd

class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d
    def __repr__(self):
        return 'Ratio({},{})'.format(self.numer, self.denom)

    def __str__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __float__(self):
        return self.numer / self.denom

    def __add__(self, other):
        if isinstance(other, int):
            n = self.numer + other * self.denom
            d = self.denom
        elif isinstance(other, float):
            return float(self) + other
        else:
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        g = gcd(n,d)
        return Ratio(n//g, d//g)

    __radd__ = __add__
