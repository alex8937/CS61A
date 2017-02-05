class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest == Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        ## return str(self.first) + " -> " + repr(self.rest)
        """
        >>> Link(2, Link(3, Link(4)))
        Link(2, Link(3, Link(4)))
        >>> Link(2)
        Link(2)
        """
        if self.rest is Link.empty:
            rest_str = ""
        else:
            rest_str = ", " + repr(self.rest)
        return "Link({0}{1})".format(self.first, rest_str)

    def __getitem__(self, index):
        """
        >>> Link(2, Link(3, Link(4)))[2]
        4
        >>> Link(2)[0]
        2
        """
        ##if index == 0:
        ##    return self.first
        ##else:
        ##    return self.rest[index - 1]
        cur = self.first
        rest = self.rest
        while index != 0:
            cur, rest, index = rest.first, rest.rest, index - 1
        return cur

    def __len__(self):
        """
        >>> len(Link(2, Link(3, Link(4))))
        3
        >>> len(Link(2))
        1
        """
        ## return 1 + len(self.rest)
        length = 1
        rest = self.rest
        while rest:
            length , rest = length + 1, rest.rest
        return length

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

    def extend_link(self, t):
        if self is Link.empty:
            return t
        else:
            return Link(self.first, Link.extend_link(self.rest, t))

    __add__ = extend_link
    __radd__ = extend_link


s = Link(2, Link(3, Link(4, Link(5))))
square = lambda x : x * x
odd = lambda x : x % 2 != 0

def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        filter_rest = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filter_rest)
        else:
            return filter_rest

def join_link(s, delimiter):
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + delimiter + join_link(s.rest, delimiter)

def partition(n, m):
    if n == 0:
        return Link(Link.empty)
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partition(n-m, m)
        with_m = map_link(lambda p : Link(m, p), using_m)
        without_m = partition(n, m-1)
        return with_m + without_m

def print_partition(n, m):
    lists = partition(n, m)
    lines = map_link(lambda s : join_link(s, ' + '), lists)
    map_link(print, lines)
