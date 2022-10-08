from Assignment2.TreeNode import TreeNode, PrintTree


def maxDepth(root):
    return getDepth(root)


def getDepth(node):
    if not node:
        return 0
    leftNode = getDepth(node.left) + 1
    rightNode = getDepth(node.right) + 1
    return max(leftNode, rightNode)


tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(maxDepth(tree))
print("==================")
printer = PrintTree()
printer.printTree(tree, 0)

