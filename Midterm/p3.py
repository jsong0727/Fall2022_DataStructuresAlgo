# In a Binary search tree print values which are inside of range.
# Optimize it if possible
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printInsideRange(self, root, small, large):
        if not root:
            return

        if root.val < small:
            self.printInsideRange(root.left, small, large)
        if root.val > large:
            self.printInsideRange(root.right, small, large)
        self.printInsideRange(root.left, small, large)
        if small <= root.val <= large:
            print(root.val)
        self.printInsideRange(root.right, small, large)


binaryTree = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)),TreeNode(10, TreeNode(9),TreeNode(14)))
solution = Solution()
solution.printInsideRange(binaryTree, 5, 8)








