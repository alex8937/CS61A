# Constructor
def tree(root, branches=[]):
    return [root] + list(branches)
# Selectors
def root(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
def is_leaf(tree):
    return not branches(tree)

def square_tree(t):
    r = root(t) ** 2
    bs = [square_tree(b) for b in branches(t)]
    return tree(r, bs)

def height(t):
    if is_leaf(t):
        return 0
    return 1 + max([height(b) for b in branches(t)])

def max_tree(t):
    if is_leaf(t):
        return root(t)
    else:
        return max(root(t), max([max_tree(b) for b in branches(t)]))
