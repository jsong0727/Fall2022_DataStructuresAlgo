from collections import deque

from Assignment2.TreeNode import TreeNode, PrintTree


def rightSideView(root):
    if not root: return []
    results = []
    queue = deque([root])
    while queue:
        node = queue[-1]
        results.append(node.val)
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return results


tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(rightSideView(tree))
print("=======================")
printer = PrintTree()
printer.printTree(tree, 0)
