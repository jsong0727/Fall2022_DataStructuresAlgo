from Assignment2.TreeNode import TreeNode, PrintTree


class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        self.dfs(root, res)
        first, second = None, None
        for i in range(len(res) - 1):
            if res[i].val > res[i + 1].val and not first:
                first = res[i]
            if res[i].val > res[i + 1].val and first:
                second = res[i + 1]
        first.val, second.val = second.val, first.val

    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            res.append(root)
            self.dfs(root.right, res)


printer = PrintTree()
root = TreeNode(1, TreeNode(3, None, TreeNode(2)))
solution = Solution()
printer.printTree(root)
print("======================")
solution.recoverTree(root)
printer.printTree(root)


