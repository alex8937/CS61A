from tree import *

def hailstone(n):
    """
    return the length of the hailstone array starting with n
    """
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n // 2) + 1
    else:
        return hailstone(n * 3 + 1) + 1

def is_int(x):
    return int(x) == x

def hailstone_tree(k, n = 1):
    """
    hailstone_tree of depth k with root n
    """
    if k == 1:
        return Tree(n)
    else:
        greater, less = n * 2, (n - 1) / 3
        branches = []
        branches.append(hailstone_tree(k - 1, greater))
        if less > 1 and less % 2 == 1 and is_int(less):
            branches.append(hailstone_tree(k - 1, int(less)))
        return Tree(n, branches)

def leaves(t):
    if t.is_leaf():
        return [t.root]
    else:
        return sum([leaves(branch) for branch in t.branches], [])

def longest_path_below(k, t):
    '''
    return longest path of a tree t and all the element in the path is below k
    '''
    if t.root > k:
        return []
    elif t.is_leaf():
        return [t.root]
    else:
        paths = [longest_path_below(k, b) for b in t.branches]
        return [t.root] + max(paths, key = len)
