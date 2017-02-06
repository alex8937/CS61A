class Yolo:
    def __init__(self, motto):
        self.motto = motto

    def g(self, num):
        return self.motto + num

def test():
    """
    >>> x = Yolo(1)
    >>> x.g(3)
    4
    >>> x.g(5)
    6
    >>> x.motto = 5
    >>> x.g(5)
    10
    """
    pass
