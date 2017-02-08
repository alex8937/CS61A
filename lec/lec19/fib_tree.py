from memo import *
from tree import *

@memo
def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.root + right.root, [left, right])

def prune_tree(t, seen = set()):
    t.branches = [branch for branch in t.branches if branch not in seen]
    seen.add(t)
    for branch in t.branches:
        prune_tree(branch, seen)
