class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PrintTree:
    def printTree(self, tree, level=0):
        if tree:
            self.printTree(tree.left, level + 1)
            print(' ' * 4 * level + '->' + str(tree.val))
            self.printTree(tree.right, level + 1)
