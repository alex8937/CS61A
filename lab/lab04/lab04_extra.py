from lab04 import *

# Q12
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    ans = []
    for elem in lst:
        if type(elem) != list:
            ans.append(elem)
        else:
            ans.extend(flatten(elem))
    return ans

# Q13
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    ans, i, j = [], 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            ans.append(lst1[i])
            i += 1
        else:
            ans.append(lst2[j])
            j += 1
    if i < len(lst1):
        ans.extend(lst1[i:])
    if j < len(lst2):
        ans.extend(lst2[j:])
    return ans
