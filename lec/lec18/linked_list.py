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
        2->3->4
        >>> Link(2)
        2
        """
        ##represent = str(self.first)
        ##rest = self.rest
        ##while rest:
        ##    represent += "->" + str(rest.first)
        ##    rest = rest.rest
        ##return represent
        if self.rest is Link.empty:
            rest = ""
        else:
            rest = "->" + repr(self.rest)
        return str(self.first) + rest

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
