def remove_all(el, lst):
    """
    >>> x = [3, 1, 2, 1, 5, 1, 1, 7]
    >>> remove_all(1, x)
    >>> x
    [3, 2, 5, 7]
    """
    i = len(lst) - 1
    while i >= 0:
        if lst[i] == el:
            lst.pop(i)
        i -= 1
