from Assignment2.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root) -> bool:

        def valid(root, left, right):
            if not root:
                return True
            if not (root.val > left and root.val < right):
                return False
            return valid(root.left, left, root.val) and valid(root.right, root.val, right)

        return valid(root, -float('inf'), float('inf'))


solution = Solution()
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(solution.isValidBST(root))