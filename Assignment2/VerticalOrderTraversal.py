from collections import deque, defaultdict

from Assignment2.TreeNode import TreeNode, PrintTree


def verticalOrder(root):
    # empty tree
    if not root:
        return []

    q = deque([(root, 0)])
    col_dict = defaultdict(list)

    while q:
        node, col = q.popleft()
        col_dict[col].append(node.val)

        if node.left:
            q.append((node.left, col - 1))
        if node.right:
            q.append((node.right, col + 1))

    res = []
    min_col = min(col_dict.keys())
    max_col = max(col_dict.keys())
    for col in range(min_col, max_col + 1):
        res.append(col_dict[col])
    return res


tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(verticalOrder(tree))
print("==========================")
printer = PrintTree()
printer.printTree(tree, 0)
