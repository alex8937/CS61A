class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, k):
        self.n += k
        return self.n

def make_adder(n):
    def adder(k):
        nonlocal n
        n += k
        return n
    return adder
