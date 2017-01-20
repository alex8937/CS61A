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

def find_path(t, x):
    def helper(t):
        if root(t) == x:
            return [x]
        else:
            path = [root(t)]
            for b in branches(t):
                if helper(b)[-1] == x:
                    path.extend(helper(b))
            return path
    return helper(t) if helper(t)[-1] == x else None



def prune(t, k):
    if k == 0:
        return tree(root(t))
    else:
        r = root(t)
        bs = [prune(b, k - 1) for b in branches(t)]
        return tree(r, bs)

def main():
    t = tree(1,
            [tree(3,
                [tree(4),
                tree(5),
                tree(6)]),
            tree(12,
                [tree(14),
                tree(15),
                tree(16)])])
    print(find_path(t, 16))
    print(find_path(t, 5))
    print(find_path(t, 7))
    print(prune(t, 1))


if __name__ == "__main__": main()
