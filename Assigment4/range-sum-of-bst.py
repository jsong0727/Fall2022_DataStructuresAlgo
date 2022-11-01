from Assignment2.TreeNode import TreeNode, PrintTree


class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def dfs(node):
            if not node: return
            if low <= node.val <= high: self.res += node.val
            if node.val > low:  dfs(node.left)
            if node.val < high: dfs(node.right)

        self.res = 0
        dfs(root)
        return self.res


root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
solution = Solution()
print(solution.rangeSumBST(root, 7, 15))
print("=============================")
printer = PrintTree()
printer.printTree(root, 0)

