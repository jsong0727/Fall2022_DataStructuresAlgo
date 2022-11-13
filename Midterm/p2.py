# 2. Populate parent of each node. in the binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    def populateParent(self, root):
        def traversal(root):
            if not root:
                return
            if root.left:
                root.left.parent = root
            if root.right:
                root.right.parent = root
            traversal(root.left)
            traversal(root.right)

        root.parent = root
        traversal(root)

solution = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
solution.populateParent(root)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.parent.val)
print(root.left.left.parent.val)
print(root.left.right.parent.val)