empty = 'empty'

def link(head, rest = empty):
    assert is_link(rest), 'rest is not a linked list'
    return [head, rest]

def is_link(s):
    return s == empty or (len(s) == 2 and is_link(s[1]))

def head(s):
    assert is_link(s), 'head only applies to linked list'
    assert s != empty, 'empty list has no head'
    return s[0]

def rest(s):
    assert is_link(s), 'head only applies to linked list'
    assert s != empty, 'empty list has no rest'
    return s[1]

def len_link(s):
    length = 0
    while s != empty:
        s, length = s[1], length + 1
    return length

def getitem_link(s, i):
    while i > 0:
        s, i = rest(s), i - 1
    return head(s)

def extend_link(s, t):
    assert is_link(s), 's is not a linked list'
    assert is_link(t), 't is not a linked list'
    if s == empty:
        return t
    else:
        return link(head(s), extend_link(rest(s), t))

def apply_to_all(fun, s):
    assert is_link(s), 's is not a linked list'
    if s == empty:
        return s
    else:
        return link(fun(head(s)), apply_to_all(fun, rest(s)))
