from Assignment2.TreeNode import TreeNode, PrintTree


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        else:
            return right


solution = Solution()
root = TreeNode(3)
p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
q = TreeNode(1, TreeNode(0), TreeNode(8))
root.left = p
root.right = q
print(solution.lowestCommonAncestor(root, p, q).val)
print("======================")
printer = PrintTree()
printer.printTree(root, 0)
