def tree(root, branches = []):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + branches

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(tree)])

def print_tree(tree, indent = 0):
    print('  ' * indent, str(root(tree)))
    for branch in branches(tree):
        print_tree(branch, indent + 1)
