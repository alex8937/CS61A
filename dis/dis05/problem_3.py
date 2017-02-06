class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4

def test():
    """
    >>> x, y = A(), B()
    >>> x.f()
    2
    >>> x.g(x, 1)
    4
    >>> y.g(x, 2)
    8
    """
    pass
