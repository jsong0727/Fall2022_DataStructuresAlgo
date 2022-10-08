from collections import deque

from Assignment2.TreeNode import TreeNode, PrintTree


def zigzagLevelOrder(root):
    if not root:
        return []
    res = []

    def levelorder(root, depth):
        if not root:
            return []
        if len(res) == depth:
            res.append([])
        if depth % 2 != 0:
            res[depth].insert(0, root.val)
        else:
            res[depth].append(root.val)
        if root.left:
            levelorder(root.left, depth + 1)
        if root.right:
            levelorder(root.right, depth + 1)

    levelorder(root, 0)

    return res

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(zigzagLevelOrder(tree))
print("=========================")
printer = PrintTree()
printer.printTree(tree)
