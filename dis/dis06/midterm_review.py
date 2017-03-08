def foo(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> foo(x)
    [0, 6, 20]
    """
    return [lst[i] * i for i in range(len(lst)) if i % 2 == 0]

def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    used = unused = 1
    for n in lst:
        used, unused = unused * n, max(unused, used)
    return max(unused, used)

class tree:
    def __init__(self, root, branches = []):
        self.root = root
        self.branches = branches

def eval_tree(tree):
    """Evaluates an expression tree with functions as root
    >>> eval_tree(tree(1))
    1
    >>> expr = tree('*', [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree('+', [expr, tree(4), tree(5)]))
    15
    """
    if not tree.branches:
        return tree.root
    if tree.root == '*':
        value = 1
        for b in tree.branches:
            value *= eval_tree(b)
        return value
    if tree.root == '+':
        value = 0
        for b in tree.branches:
            value += eval_tree(b)
        return value

def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = quicksort_list([x for x in lst[1:] if x <= pivot])
    greater = quicksort_list([x for x in lst[1:] if x > pivot])
    return less + [pivot] + greater


def quicksort_link(link):
    """
    >>> s = Link(3, Link(1, Link(4)))
    >>> quicksort_link(s)
    Link(1, Link(3, Link(4)))
    """
    if _____________________________________________________:
        return link
    pivot, _______ = ________________________________________
    less, greater = _________________________________________
    while link is not Link.empty:
        curr, rest = link, link.rest
        if _________________________________________________:
            _________________________________________________
        else:
            _________________________________________________
        link = ______________________________________________
    less = __________________________________________________
    greater = _______________________________________________
    _________________________________________________________
    return __________________________________________________
