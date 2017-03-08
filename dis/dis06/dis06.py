class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)
    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> unique = remove_duplicates(lnk)
    >>> len(unique)
    2
    >>> len(lnk)
    2
    """
    cur = lnk
    while cur.rest:
        if cur.first == cur.rest.first:
            cur.rest = cur.rest.rest
        else:
            cur = cur.rest
    return lnk

def reverse(lnk):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> r = reverse(a)
    >>> r.first
    3
    >>> r.rest.first
    2
    """
    # if lnk == Link.empty or lnk.rest == Link.empty:
    #     return lnk
    # rst = lnk.rest
    # head = reverse(rst)
    # rst.rest = lnk
    # return head
    pre = Link.empty
    cur = lnk
    while cur:
        nxt = cur.rest
        cur.rest = pre
        pre = cur
        cur = nxt
    return pre

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """
    value = 1
    for i in range(len(lst_of_lnks)):
        if lst_of_lnks[i] == Link.empty:
            return Link.empty
        value *= lst_of_lnks[i].first
        lst_of_lnks[i] = lst_of_lnks[i].rest
    return Link(value, multiply_lnks(lst_of_lnks))
