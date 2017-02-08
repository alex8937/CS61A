class Tree:
    def __init__(self, root, branches = []):
        self.root = root
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches
    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            return 'Tree({}{})'.format(self.root, repr(self.branches))
        else:
            return 'Tree({})'.format(self.root)

    def indented(self, k = 0):
        lines = []
        lines.append('  ' * k + str(self.root))
        for branch in self.branches:
            lines.extend(branch.indented(k + 1))
        return lines

    def __str__(self):
        return '\n'.join(self.indented())
