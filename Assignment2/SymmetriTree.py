from Assignment2.TreeNode import TreeNode, PrintTree


def isSymmetric(root):
    if not root:
        return True
    return compare(root.left, root.right)


def compare(left, right):
    if not left and right:
        return False
    elif not right and left:
        return False
    elif not left and not right:
        return True
    elif left.val != right.val:
        return False

    outside = compare(left.left, right.right)
    inside = compare(left.right, right.left)
    return outside and inside


tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(isSymmetric(tree))
printer = PrintTree()
printer.printTree(tree, 0)
